#! /usr/bin/env python

import argparse
import keyring
import getpass

def get_value(service, username):
    print keyring.get_password(service, username)

def set_value(value, service, username):
    keyring.set_password(service, username, value)

parser = argparse.ArgumentParser(
    usage="keyring [arg] arg\n\
        get and set values in keychain", prog="keychain 0.0.1")

parser.add_argument('-g', dest="get", action='store', nargs='+', help='get a value, args: \
    <service> [username|$USER]')
parser.add_argument('-s', dest="set", action='store', nargs='+', help='save a value, args: \
    <value> <service> [username|$USER]')

opts = parser.parse_args()

if opts.get != None:
    if len(opts.get) == 1:
        username = getpass.getuser()
    else:
        username = opts.get[1]
    get_value(opts.get[0], username)
elif opts.set != None:
    if len(opts.set) == 2:
        username = getpass.getuser()
    else:
        username = opts.set[2]
    set_value(opts.set[0], opts.set[1], username)