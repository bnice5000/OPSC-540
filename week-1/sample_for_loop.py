#!/usr/bin/env python

""" sample_for_loop project for OPSC-540 week 1

This is a small assignment file for OPSC-540 week 1 that teaches about list and string manipulation.

__author__ = "Brian Levin"
__copyright__ = "Copyright 2022, Brian Levin"
__credits__ = ["Brian Levin", "Todd Strunce"]
__license__ = "AGPL"
__version__ = "0.0.1"
__maintainer__ = "Brian Levin"
__email__ = "brian4lawschool@gmail.com"
__status__ = "Assignment"
"""

def format_list_to_oxford_str_loop(list_input):
    """Takes a list and converts it to a oxford comma separated string using a loop.

    Args:
        list_input (list): A list made of any data type or types.

    Returns:
        string: a string of the list elements formatted in oxford comma format.
    """
    str_comma_space = ", "
    str_and = ", and "
    str_return = ""

    for index, element in enumerate(list_input):
        if index == len(list_input) - 2:
            str_return = str_return + element + str_and + list_input[index + 1]
        if index != len(list_input) - 1 and index != len(list_input) - 2:
            str_return = str_return + element + str_comma_space

    return str_return

def format_list_to_oxford_str(list_input):
    """Takes a list and converts it to a oxford comma separated string.

    Args:
        list_input (list): A list made of any data type or types.

    Returns:
        string: a string of the list elements formatted in oxford comma format.
    """
    return f"{', '.join(list_input[:-1])}, and {list_input[-1]}"

if __name__ == "__main__":
    spam = ["apples", "bananas", "tofu", "cats"]

    SPAM_STR = format_list_to_oxford_str_loop(spam)

    # for spam_item in spam:
    #     print("\n\nSpam item: " + spam_item)
    #     SPAM_STR = SPAM_STR + spam_item
    #     print("Spam str: " + SPAM_STR + "\n\n")

    print(SPAM_STR)

    cities = ["New York", "Chicago", "Atlanta", "Burlington", "Philadelphia", "Denver"]

    CITIES_STR = format_list_to_oxford_str_loop(cities)

    # manipulate cities list here

    print(CITIES_STR)

    food = ["carrots", "mango", "avocado"]

    FOOD_STR = format_list_to_oxford_str_loop(food)

    # manipulate food list here

    print(FOOD_STR)
