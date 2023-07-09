"""
Utilities for loading data
"""

import os, sys
from pathlib import Path
import wget

IN_COLAB = 'google.colab' in sys.modules
BASE_URL = "https://raw.githubusercontent.com/hnguyentt/dataisbeautiful/master/assets/data/"


def get_datapath(filename):
    """
    Check if IN_COLAB --> check if file exists in CWD, if not download --> return filepath
    :param filename:
    :return:
    """
    if IN_COLAB:
        path = Path(filename)
        if not path.exists():
            wget.download(f'{BASE_URL}/{filename}', filename)
    else:
        path = Path(f"../assets/data/{filename}")

    return path


