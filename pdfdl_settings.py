"""
Module containing base settings
"""

import logging
from enum import Enum

# System setup
log = logging.getLogger(__name__)

class Settings(Enum):
    """
    Set global settings
    """
    default_excel_prefix = "GRI_"
