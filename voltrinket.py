#!/usr/bin/env python
# Copyright (c) 2014 Xavier Mendez
# All rights reserved.

# This file is part of Voltrinket.
#
# Voltrinket is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Voltrinket is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with Voltrinket.  If not, see <http://gnu.org/licenses/>.

"""Voltrinket host reader.

Usage:
  voltrinket.py [-r | --raw] [-v | --verbose]
  voltrinket.py (-h | --help)
  voltrinket.py --version

Options:
  -r --raw      Print the raw values instead of lectures in Volts (V).
  -A --no-ansi  Don't use ANSI escape sequences for color and scrollback.
  -v --verbose  Show additional info.
  -q --quiet    Don't show any status messages.

  -h --help     Show this help text.
  -V --version  Show the program's version.

"""

from docopt import docopt
import time, select
import usb.core, usb.util

# The Trinket is expected to emit that same footprint
# at start, in order for the program to pick its data.
FOOTPRINT = "Voltrinket 0.1.0"

if __name__ == '__main__':
    args = docopt(__doc__, version=FOOTPRINT)
    try:
        while True: loop()
    except InterruptError:
        print()

def loop():

    # 1. Try to find and connect to a Trinket

    if args.verbose:
        print("Waiting for a Trinket...")

    while True:
        trinket = usb.core.find(idVendor = 0x1781, idProduct = 0x1111)
        if trinket: break
        time.sleep(0.1) # don't hog all CPU

    trinket.setConfiguration()

    if args.verbose:
        print("Connected to a Trinket.")


    # 2. Check footprint and read the data

    #endpoint = 0x81
    endpoint = trinket[0][(0,0)][0] # the first endpoint should be the only endpoint, it should be an interrupt-in endpoint

    while True:
        time.sleep(0.01) # don't hog all CPU
        try:
            data = trinket.read(endpoint.bEndpointAddress, endpoint.wMaxPacketSize)
            # TODO

        except Exception as ex:
            exStr = str(ex).lower()

            # for timeouts: wait a bit, then continue reading
            if 'timeout' in exStr:
                time.sleep(0.01)
                continue

            # any other error: disconnect
            if not args.silent:
                print 'USB read error: ', ex
            break


     if args.verbose:
         print("Disconnected from the Trinket.")
