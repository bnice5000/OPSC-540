"""Week 5 Discussion - Regex hostname or IP

Application checks if it is a hostname or IP

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
import validators


def is_ipv4(str_ip_address):
    """Checks if a string is a valid IPv4 address

    Args:
        str_ip_address (string): a string that may be an IPv4 address

    Returns:
        bool: the result of the test as to whether it is an IPv4
    """

    REGEX_IP = re.compile(r"^((25[0-5]|(2[0-4]|1\d|[1-9]|)\d)\.?\b){4}$")

    return bool(re.search(REGEX_IP, str_ip_address))


def is_hostname(str_hostname):

    """Checks if a string is a valid hostname address

    Args:
        str_hostname (string): a string that may be an hostname address

    Returns:
        bool: the result of the test as to whether it is an hostname
    """

    REGEX_HOSTNAME = re.compile(
        r"^(([a-zA-Z]|[a-zA-Z][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z]|[A-Za-z][A-Za-z0-9\-]*[A-Za-z0-9])$"
    )

    return bool(re.search(REGEX_HOSTNAME, str_hostname))


print(is_ipv4("127.0.0.1"))
print(is_ipv4("300.0.0.1"))

print(is_hostname("www.google.com"))
print(is_hostname("me@you.com"))

print(validators.ipv4("127.0.0.1"))
print(bool(validators.ipv4("300.0.0.1"))) # for the purpose of this example we coerce the exception into a bool

print(validators.domain("www.google.com"))
print(bool(validators.domain("me@you.com"))) # for the purpose of this example we coerce the exception into a bool
