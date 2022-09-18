#!/usr/bin/env python

""" collatz project for OPSC-540 week 2

This file correctly implements the collatz conjecture as a week 2 project for OPSC-540.

__author__ = "Brian Levin"
__copyright__ = "Copyright 2022, Brian Levin"
__credits__ = ["Brian Levin", "Todd Strunce"]
__license__ = "AGPL"
__version__ = "0.0.1"
__maintainer__ = "Brian Levin"
__email__ = "brian4lawschool@gmail.com"
__status__ = "Assignment"
"""


def is_even(number):
    """Check if number is even.

    Args:
        number (int): Any integer

    Returns:
        bool: if the number modulus 2 equal zero, it returns true , otherwise it returns false.
    """
    return number % 2 == 0


def check_number(number):
    """Takes a number and iterates it based on the collatz pattern.

    Args:
        number (int): a positive integer

    Returns:
        int: the result of the collatz process
    """
    if is_even(number):
        number = number // 2
    else:
        number = 3 * number + 1

    return number


def collatz(number):
    """Takes a number and loops until it equals 1.

    Args:
        number (int): a positive integer
    """

    while number != 1:
        print(number)
        number = check_number(number)
    print("Final number is: " + str(number))


if __name__ == "__main__":
    user_input = abs(int(input("Enter a number:")))
    collatz(user_input)
