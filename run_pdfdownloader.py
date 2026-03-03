"""
Script for starting PDF Downloader.

Adds some testing and logging options.
"""
# pylint: disable=no-name-in-module
#         Pylint is unable to locate perfectly normal members of perfectly
#         normal modules. Explanations for this remain elusive.


#
# Dependencies
# ============
#

# Standard libraries
import sys
import argparse
import logging
from logging.config import dictConfig
import pytest
import yaml


LOGGER = logging.getLogger(__name__)

#
# Control / Command-line parsing
# ==============================
#

# Argument parsing
if __name__ == '__main__':
    PARSER = argparse.ArgumentParser(description='A program for automatically downloading pdf files.')
    PARSER.add_argument("-t", "--test",
                        help="Run tests of pdf downloader",
                        action="store_true")
    PARSER.add_argument("-v", "--verbosity", action="count", default=0,
                        help="Verbosity level; v to vvv")
    PARSER.add_argument("-l", "--filter", action="store", dest="module",
                        default="", help="Filter logging to arbitrary module")
    # Need option for naming excel file to read
    ARGS = PARSER.parse_args()

    # Setting logger verbosity
    # logger level can be one of DEBUG|INFO|WARNING|ERROR|CRITICAL
    if ARGS.verbosity == 0:
        LOGGING_LEVEL = logging.ERROR
    elif ARGS.verbosity == 1:
        LOGGING_LEVEL = logging.WARNING
    elif ARGS.verbosity == 2:
        LOGGING_LEVEL = logging.INFO
    elif ARGS.verbosity >= 3:
        LOGGING_LEVEL = logging.DEBUG
    with open('logging_configuration.yaml', 'r') as f:
        CONFIG_DICT = yaml.safe_load(f.read())
        CONFIG_DICT['handlers']['console']['level'] = LOGGING_LEVEL
        CONFIG_DICT['handlers']['console']['filters'] = ['special']
        CONFIG_DICT['filters'] = {}
        CONFIG_DICT['filters']['special'] = {}
        CONFIG_DICT['filters']['special']['()'] = logging.Filter
        CONFIG_DICT['filters']['special']['name'] = ARGS.module
        dictConfig(CONFIG_DICT)

    if ARGS.test:
        pytest.main(["test_pdfdownloader.py"])
        sys.exit()
    else:
        # call program w args
        pass
        # pdfdownload(ARGS.etc)
    sys.exit()
