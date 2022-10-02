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


import hashlib


def main():

    """Check hashes.txt for matching password in password.lst
    """

    list_answers = []

    with open("hashes.txt", "r", encoding="ascii") as reader:
        list_hashes = [hashes.strip() for hashes in reader]

    with open("password.lst", "r", encoding="ascii") as reader:
        dict_password = dict([(hashlib.md5(password.strip().encode("utf-8")).hexdigest(), password.strip()) for password in reader])

    for str_hash in list_hashes:
        if str_hash in dict_password:
            list_answers.append(dict_password[str_hash])

    with open("answers.txt", "w", encoding="ascii") as writer:
        writer.write('\n'.join(list_answers) + '\n')



if __name__ == "__main__":
    main()
