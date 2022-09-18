#!/usr/bin/env python

""" ssl_client project for OPSC-540 week 2

This file creates and executes an ssl client as a week 2 project for OPSC-540.

__author__ = "Brian Levin"
__copyright__ = "Copyright 2022, Brian Levin"
__credits__ = ["Brian Levin", "Todd Strunce"]
__license__ = "AGPL"
__version__ = "0.0.1"
__maintainer__ = "Brian Levin"
__email__ = "brian4lawschool@gmail.com"
__status__ = "Assignment"
"""

import socket
import ssl

HOST = "localhost"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

# Handle issues with self signed certs
ssl.SSLContext.verify_mode = property(
    lambda self: ssl.CERT_NONE, lambda self, newval: None
)

# Create a context and add the cert to the context.
# This is necessary because it is a self signed cert.
context = ssl.create_default_context()
context.load_verify_locations("./cert.pem")

# Use the context to open the socket and encrypt the socket.
# Send data and receive response.
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    with context.wrap_socket(sock, server_hostname=HOST) as sec_sock:
        sec_sock.connect((HOST, PORT))
        sec_sock.sendall(b"Hello, world")
        data = sec_sock.recv(1024)

print(f"Received {data!r}")
