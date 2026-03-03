"""
Module containing the pdfdownloader.

Purpose:
Automate the downloading of pdf files.

How:
Read links from excel file, download those assuming they are referring to pdf files.
Make a working copy of the excel file, mark status for links when downloads are attempted whether failed or succeeded.
"""

import logging

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

def download_pdfs( pdf_file="" ):
    """
    Function that starts the downloading process
    """
    pass
