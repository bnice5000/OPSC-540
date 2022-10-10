#!/usr/bin/env python

""" scraping for OPSC-540 week 5

Follows the very interesting assignment 5's logic to its inevitable conclusion.

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

from bs4 import BeautifulSoup
import requests


def main():
    """ The main method.

    Searches the below webpage for specific a tags and login forms input fields.
    """

    STR_URL = "https://www.champlain.edu/current-students"

    obj_page = requests.get(STR_URL)

    if obj_page.status_code == 200:

        # instantiate the bs4 soup parser
        obj_soup = BeautifulSoup(obj_page.text, "html.parser")

        # find the tags by class
        list_a_tags = obj_soup.find_all("a", class_="section-link")
        list_login_tags = obj_soup.find_all("input", {"id": re.compile("login-.*")})

        # print the formatted output
        print('The assignment "a" tags are as follows:')
        print(*list_a_tags, sep="\n")
        print('The login "input" tags are as follows:')
        print(*list_login_tags, sep="\n")

    else:
        print(f"There is an issue with the page. Status code: {obj_page.status_code}")


if __name__ == "__main__":
    main()
# end main
