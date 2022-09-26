#!/usr/bin/env python

""" file_manipulation for OPSC-540 week 3

Follows the very interesting assignment 3's logic to its inevitable conclusion.

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

import argparse
import itertools
import os
import platform
import subprocess
import sys


def is_posix():
    """Checks the operating system to see if it is posix.

    Returns:
        bool: If posix, returns true. Else returns false.
    """
    operating_system = platform.system()
    if operating_system == "Linux" or operating_system == "Darwin":
        return True
    else:
        return False


def print_platform_information():
    """prints platform information"""
    print(f"{platform.system()} {platform.release()} {platform.version()}")


def search_etc_passwd(terms):
    """Searches /etc/passwd for a specific username

    Args:
        terms (tuple): The terms to search the file

    Returns:
        List: returns a list containing the matching lines or an empty list
    """
    passwd_location = "/etc/passwd"
    if os.path.exists(passwd_location):
        with open(passwd_location, "r", encoding="utf8") as passwd_file:
            lines = passwd_file.readlines()

        match_lines = [line for line in lines if line.startswith(terms)]
        return match_lines
    else:
        return []


def write_output(lines, file):
    """writes the matching lines to the specified file

    Args:
        lines (list): a list of the lines to be written to the file
        file (string): the file to be written to
    """
    with open(file, "w", encoding="utf8") as out_file:
        out_file.writelines(lines)


def convert_input(fat_list):
    """converts list in list into a flat tuple

    Args:
        fat_list (list): a list of lists

    Returns:
        tuple: a flattened tuple of the lists
    """
    return tuple(list(itertools.chain(*fat_list)))


def main():
    """The main function that executes the program"""

    # Create the parser
    parser = argparse.ArgumentParser(description="Read passwd file.")
    parser.add_argument("-f", "--file", type=str, help="output file", required=True)
    parser.add_argument(
        "-u",
        "--user",
        action="append",
        nargs="+",
        type=str,
        help="username",
        required=True,
    )

    # Parse arguments
    args, leftovers = parser.parse_known_args()

    # Check if the operating system is POSIX
    if not is_posix():
        print("OS is not supported.")
    else:
        # If it is POSIX print the platform information
        print_platform_information()

        # Check for the required args
        if args.file is not None and args.user is not None:

            # Convert user arguments into a flat tuple
            flat_tuple = convert_input(args.user)
            passwd_results = search_etc_passwd(flat_tuple)

            # Check if the list is empty.
            # If it has results write them to file
            # Else tell user search was empty
            if passwd_results:
                write_output(passwd_results, args.file)
            else:
                print("Search was empty!")

    user_input = os.path.normpath(input("Please enter a file name:"))
    if os.path.exists(user_input):
        results = subprocess.check_output(
            f"ls -l {user_input};id",
            stderr=subprocess.STDOUT,
            shell=True,
            encoding="UTF-8",
        )
        print(f"{results}")
        try:
            results = subprocess.check_output(
                f"ls {user_input};id", stderr=subprocess.STDOUT, encoding="UTF-8"
            )
            print(f"{results}")
        except Exception as exc:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(f"Error caught: {exc}")
            print(f"Error {exc_type}, file: {fname}, line:{exc_tb.tb_lineno}")
            print("Error gracefully caught!")


if __name__ == "__main__":
    main()
# end main
