#!/usr/bin/env python

""" ssl_server project for OPSC-540 week 2

This file creates and executes an ssl server as a week 2 project for OPSC-540.

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

HOST = "localhost"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

# Handle issues with self signed certs
ssl.SSLContext.verify_mode = property(
    lambda self: ssl.CERT_NONE, lambda self, newval: None
)

# Create a context and add the cert to the context.
# This is necessary because it is a self signed cert.
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain("./cert.pem", "./key.pem")

# Use the context to open the socket and encrypt the socket.
# Receive data and echo it back to the client.
with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as sock:
    sock.bind((HOST, PORT))
    sock.listen(5)
    with context.wrap_socket(sock, server_side=True) as sec_sock:
        conn, addr = sec_sock.accept()
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
