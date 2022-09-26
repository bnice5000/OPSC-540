#!/usr/bin/env python

""" file_manipulation for OPSC-540 week 3

Checks magic file two different ways and returns results.

__author__ = "Brian Levin"
__copyright__ = "Copyright 2022, Brian Levin"
__credits__ = ["Brian Levin", "Todd Strunce"]
__license__ = "AGPL"
__version__ = "0.0.1"
__maintainer__ = "Brian Levin"
__email__ = "brian.levin@mymail.champlain.edu"
__status__ = "Assignment"
__note__ = "This is experimental and could use error handling. Use at your own peril!"
"""


import os
import subprocess

import magic


def file_lookup(file_loc):
    """Looks up the file type by calling out to subprocess

    Args:
        file_loc (string): file location and name

    Returns:
        string: file type
    """
    # Checks to see if the file exists
    if os.path.exists(file_loc):
        # Runs the subprocess and captures the result
        result = subprocess.run(["file", file_loc], stdout=subprocess.PIPE, check=True)
        # Returns the result. However, the result is coded in binary and has a new line.
        # Decodes the binary to ASCII and removes the newline
        return result.stdout.decode("ascii").strip()
    else:
        print("File does not exist")


def file_lookup_magic(file_loc):
    """Looks up the file type by using the magic library and libmagic.

    Args:
        file_loc (string): file location and name

    Returns:
        string: file type
    """
    # Checks to see if the file exists
    if os.path.exists(file_loc):
        # Returns the result of the magic file.
        return magic.from_file(file_loc)
    else:
        print("File does not exist")


if __name__ == "__main__":
    FILE_NAME = "./test_doc.docx"
    ret_val_reg = file_lookup(FILE_NAME)
    ret_val_magic = file_lookup_magic(FILE_NAME)

    print(f"The subprocess output: {ret_val_reg}")
    print(f"The magic output {ret_val_magic}")
