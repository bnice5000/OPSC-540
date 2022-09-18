#!/usr/bin/env python

""" network_sweep for OPSC-540 week 2

This file ping sweeps a network and then checks a list of
specific ports as a week 2 project for OPSC-540.

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

import socket
import subprocess


def port_scanner(server_ip, ports):
    """Takes active IP and check a list of ports for response.

    Args:
        server_ip (string): the string representation of an IP address
        ports (list): A list of port to check at the IP address
    """

    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((server_ip, port))
        if result == 0:
            print(f"Port {port} is open.")
        sock.close()


if __name__ == "__main__":

    # Port list for scanning
    port_list = [21, 23, 80, 513]

    # Clear the screen
    subprocess.call("clear", shell=True)

    # Get user input for the IP range
    # ip_range = int(input("What is the maximum bounds of the scan range: "))
    ip_range = 25

    # Loop over the range and ping the IPs that have been selected
    for last_digit in range(1, ip_range):

        # Set the constants of the address and the result of the ping
        ADDRESS = f"10.9.8.{last_digit}"
        RESULTS = subprocess.call(
            ["ping", "-c", "1", ADDRESS],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.STDOUT,
        )

        # Check the result of the ping. If it is positive for a host, run port scanner function.
        if RESULTS == 0:
            print(f"Host Found {ADDRESS}:")
            port_scanner(ADDRESS, port_list)
        else:
            print(f"No Host Found {ADDRESS}!")
