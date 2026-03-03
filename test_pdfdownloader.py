"""
Test module.

All *test* functions are executed automatically by pytest.
Any @pytest.fixture functions, when named as parameter, brings in the result
of the fixture function as parameter for the given test function.
"""
# pylint: disable=redefined-outer-name, no-name-in-module
#         ref-out-name:
#         Pytest does some automatic decoration for ease of use;
#         presumably this is what pylint catches on to and complains
#         about.
#         no-name-in:
#         Pylint is unable to locate perfectly normal members of perfectly
#         normal modules. Explanations for this remain elusive.

# Standard libraries
import faulthandler
import logging
import pytest
import pdfdownloader
import os

logger = logging.getLogger("__name__")

# Internal code


@pytest.fixture(scope="function")
def setup():
    """
    Populates stack with initial data for later testing.
    """
    faulthandler.enable(open("core.dump", 'w'))
    testdata = "Something complicated"
    return testdata


def test_download_1(setup):
    """
    Test if pdf downloads work as expected.
    """
    results = pdfdownloader.download_pdfs([
        "https://example.com/example.pdf",
        "notthere",
        "https://windigo.pdf",
        "vendsyssel",
        "https://www.niti.gov.in/sites/default/files/2024-07/SDG_India_Index_2023-24.pdf",
        "https://ncert.nic.in/textbook/pdf/leac204.pdf",
        "https://www.macfarlanegroup.com/wp-content/uploads/2025/09/Macfarlane-Group-PLC-Interim-Report-2025.pdf",
        "https://corporate.ralphlauren.com/on/demandware.static/-/Sites-RalphLauren_Corporate-Library/default/dw101f5a7d/assets/images/PRESS_RELEASES/InvestorDay2025.pdf",
        "https://amotiv.com/uploads/documents/802/250916---Notice-of-Annual-General-Meeting-2025.pdf"
    ])
    expected = ['error', 'error', 'error', 'error',
                'success', 'success', 'success', 'success', 'success']
    assert( len(expected) == len(results) )
    comparison_list = []
    for i in range(len(expected)):
        comparison_list.append( (expected[i], results[i]['status']) )
    for exp, res in comparison_list:
        logger.debug( f"Expected: {str(exp)} - Received: {str(res)}" )
        assert( exp == res )

def test_excel_1(setup):
    """
    Test if excel file reading and writing works as expected.
    """
    dataframe = pdfdownloader.load_dataframe( "excel-data/GRI_2017_2025.xlsx", [0, 1, 2])
    logger.debug( f"\nDataframe:\n{ dataframe }" )
    assert( len(dataframe) == 271 )

def test_excel_2(setup):
    firstname = 'Alice'
    lastage = 25
    test_file = 'excel-data/testfile.xlsx'
    new_rows = [{'Name': firstname, 'Age': 30}, {'Name': 'Bob', 'Age': lastage}]
    new_frame = pdfdownloader.append_row( test_file, new_rows)
    logger.debug(f"\nDataframe to add to file:\n{ str(new_frame) }")
    assert(os.path.exists( test_file ))
    written_df = pdfdownloader.load_dataframe( test_file, [0, 1] )
    logger.debug(f"\nDataframe of file after appending:\n{ str(written_df) }")
    logger.debug(f"{ written_df.iat[0, 0] }")
    logger.debug(f"{ written_df.iat[1, 1] }")
    assert( written_df.iat[0, 0] == firstname )
    assert( written_df.iat[1, 1] == lastage )
    file_ops = False
    try:
        os.remove( test_file )
        file_ops = True
    except FileNotFoundError:
        logger.debug(f"File '{ test_file }' not found")
    except PermissionError:
        logger.debug(f"Permission denied to delete '{ test_file }'")
    except OSError as e:
        logger.debug(f"Error deleting '{ test_file }': {e}")
    assert( file_ops )
