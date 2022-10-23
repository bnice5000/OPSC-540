#!/usr/bin/env python

""" network_sweep for OPSC-540 week 7

Trying to figure out the mod_security logs assignment for week 7 project for OPSC-540.

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

import sqlalchemy as db


def read_file(filename):
    """Reads in a file

    Args:
        filename (string): the name of the file to be read into the application

    Returns:
        list[string]: a list of the lines of the file in string format
    """

    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()

    return lines


def write_database(hacks):
    """Write information to database

    Args:
        hacks (list[{type: type of hack, instance: example of the hack}]): a list of dictionary of string
    """

    engine = db.create_engine("sqlite:///hacks.sqlite")
    connection = engine.connect()
    metadata = db.MetaData()
    hack_table = db.Table(
        "hacks",
        metadata,
        db.Column("id", db.Integer, primary_key=True),
        db.Column("type", db.String),
        db.Column("instance", db.String),
    )
    metadata.create_all(engine)
    query = db.insert(hack_table)
    results = connection.execute(query, hacks)
    results.close()
    connection.close()
    engine.dispose()


def main():
    """the main function that controls the application
    """
    log_file = read_file("modsec_audit.log.1")
    hack_list = []

    for idx, line in enumerate(log_file):
        if "-B--" in line:
            potential_hack = log_file[(idx + 1) % len(log_file)]
            if "../" in potential_hack:
                hack_list.append({"type": "traversal", "instance": potential_hack})
            elif "rfi" in potential_hack:
                hack_list.append(
                    {"type": "Remote File Inclusion", "instance": potential_hack}
                )
            elif "DBMS" in potential_hack:
                hack_list.append({"type": "SQL Injection", "instance": potential_hack})
            elif ".htaccess" in potential_hack:
                hack_list.append(
                    {"type": "htaccess accessible", "instance": potential_hack}
                )
            else:
                hack_list.append({"type": "Unidentified", "instance": potential_hack})

    write_database(hack_list)

if __name__ == "__main__":
    main()
    # end main
