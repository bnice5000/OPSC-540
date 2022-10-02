#!/usr/bin/env python

"""check_strength_sample for OPSC-540 week 4

Checks password strength against basic standards.

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

import re


def main():
    """Program that checks a user password for strength."""

    with open("answers.txt", "r", encoding="ascii") as file:
        lines = [line.strip() for line in file]

    REGEX_LOWER = re.compile(r"[a-z]")  # Please add your lower alpha re here
    REGEX_UPPER = re.compile(r"[A-Z]")  # Please add your upper alpha re here
    REGEX_NUMBER = re.compile(r"[0-9]")  # Please add your number re here
    REGEX_SPECIAL = re.compile(r"[^\w\s]")  # Please add your special character

    for str_password in lines:
        bool_is_good_len = False
        bool_has_lower = False
        bool_has_upper = False
        bool_has_number = False
        bool_has_special = False
        int_password_score = 0

        if len(str_password) > 6:  # check for number of characters > 6
            bool_is_good_len = True
            int_password_score += 1
        if re.search(REGEX_LOWER, str_password):  # lowercase alpha search
            bool_has_lower = True
            int_password_score += 1
        if re.search(REGEX_UPPER, str_password):  # upper alpha search
            bool_has_upper = True
            int_password_score += 1
        if re.search(REGEX_NUMBER, str_password):  # numbers search
            bool_has_number = True
            int_password_score += 1
        if re.search(REGEX_SPECIAL, str_password):  # special characters
            bool_has_special = True
            int_password_score += 1
        print(f"results for {str_password}: score: {int_password_score}")
        print(
            f"good_len: {bool_is_good_len}, lower: {bool_has_lower}, upper: {bool_has_upper}, num: {bool_has_number}, special: {bool_has_special}"
        )
    # end main


if __name__ == "__main__":
    main()
