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
    return number % 2 == 0

def check_number(number):
    if is_even(number):
        number = number // 2
    else:
        number = 3 * number + 1

    return number

def collatz(number):
    while number != 1:
        print(number)
        number = check_number(number)
    print("Final number is: " + str(number))



if __name__ == "__main__":
    user_input = abs(int(input("Enter a number:")))
    collatz(user_input)
