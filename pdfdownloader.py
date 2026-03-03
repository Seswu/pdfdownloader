"""
Module containing the pdfdownloader.

Purpose:
Automate the downloading of pdf files.

How:
Read links from excel file, download those assuming they are referring to pdf files.
Make a working copy of the excel file, mark status for links when downloads are attempted whether failed or succeeded.
"""


import logging
import pandas as pd
import os
import requests
from pathlib import Path
from typing import List, Dict, Tuple
from urllib.parse import urlparse


# System setup
log = logging.getLogger(__name__)


class DownloadError(Exception):
    """
    Exception raised for unfavourable results during download, such as it failing,
    getting the wrong file type or the process hanging indefintely.
    """
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

def load_dataframe( file_path, column_names ):
    """
    Reads specified columns from an Excel file using pandas.

    Args:
        file_path (str): Path to the Excel file
        column_names (list): List of column names or indices to read

    Returns:
        pd.DataFrame: DataFrame with the specified columns

    Example usage:
    data = read_excel_columns('data.xlsx', ['Column1', 'Column2', 'Column3'])
    """
    df = pd.read_excel(file_path, usecols=column_names)
    return df

def append_row( file_path, data, sheet='Sheet1' ):
    """
    Appends new data rows to an Excel file.

    Args:
        file_path (str): Path to the Excel file
        new_data (pd.DataFrame or dict/list): Data to append (auto-converted to DataFrame)
        sheet_name (str): Target sheet name

    Returns:
        new_df: DataFrame that was added to the Excel file

    # Example usage:
    new_rows = [{'Name': 'Alice', 'Age': 30}, {'Name': 'Bob', 'Age': 25}]
    append_to_excel('data.xlsx', new_rows)
    """

    # Convert to DataFrame if needed
    if not isinstance(data, pd.DataFrame):
        new_df = pd.DataFrame(data)
    else:
        new_df = data

    if os.path.exists(file_path):
        # Read existing data
        existing_df = pd.read_excel( file_path, sheet_name=sheet )
        # Combine and save
        combined_df = pd.concat( [existing_df, new_df], ignore_index=True )
        combined_df.to_excel( file_path, sheet_name=sheet, index=False )
    else:
        # Create new file
        new_df.to_excel( file_path, sheet_name=sheet, index=False )

    return new_df

def download_pdfs(urls: List[str], base_dir: str = "downloads") -> List[Dict[str, str]]:
    """
    Downloads multiple PDFs from URLs and returns results for further processing.

    Args:
        urls: List of PDF URLs
        base_dir: Directory to save files

    Returns:
        List of dicts: [{'url': str, 'path': str, 'status': 'success|error', 'message': str}]
    """

    Path(base_dir).mkdir(parents=True, exist_ok=True)
    results = []

    for url in urls:
        try:
            # Extract filename from URL or use generic name
            parsed = urlparse(url)
            filename = os.path.basename(parsed.path)
            if not filename or not filename.lower().endswith('.pdf'):
                filename = f"document_{len(results)+1}.pdf"

            filepath = os.path.join(base_dir, filename)

            # Download with progress feedback
            response = requests.get(url, stream=True, timeout=30)
            response.raise_for_status()

            # Verify content type is PDF
            content_type = response.headers.get('content-type', '').lower()
            if 'pdf' not in content_type:
                results.append({
                    'url': url,
                    'path': None,
                    'status': 'error',
                    'message': f"Not a PDF (content-type: {content_type})"
                })
                continue

            # Save file
            with open(filepath, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)

            results.append({
                'url': url,
                'path': filepath,
                'status': 'success',
                'message': f"Downloaded ({response.headers.get('content-length', 'unknown')} bytes)"
            })
            logging.debug(f"✓ {filename} saved")

        except requests.RequestException as e:
            results.append({
                'url': url,
                'path': None,
                'status': 'error',
                'message': f"Download failed: {str(e)}"
            })
            logging.debug(f"✗ {url}: {str(e)}")

    return results
