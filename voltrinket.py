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
  voltrinket.py [options]

Options:
  -r --raw      Print the raw values instead of lectures in Volts (V).
  -A --no-ansi  Don't use ANSI escape sequences for color and scrollback.
  -v --verbose  Show additional info.
  -q --quiet    Don't show any status messages.

  -h --help     Show this help text.
  -V --version  Show the program's version.

"""

from docopt import docopt
import time, select, sys
import usb.core, usb.util

def loop():

    # 1. Try to find and connect to a Trinket

    if args["--verbose"]:
        print("Waiting for a Trinket...")

    while True:
        trinket = usb.core.find(idVendor = 0x1781, idProduct = 0x1111)
        if trinket: break
        time.sleep(0.1) # don't hog all CPU

    trinket.set_configuration()
    endpoint = trinket[0][(0,0)][0] # the first endpoint should be the only endpoint, it should be an interrupt-in endpoint

    if not args["--quiet"]:
        print("Connected to a Trinket.")


    # 2. Check footprint and read the data

    if not args["--raw"]:
        if args["--no-ansi"]:
            format = "Voltage: %.3fV"
        else:
            format = "\x1b[F\x1b[JVoltage: %.3fV"
            print("Voltage: ------")

    cleared = False
    while True:
        try:
            # read next line
            line = bytearray()
            while True:
                c = endpoint.read(1)[0]
                if c == ord('\n'): break
                line.append(c)

            # make sure we have read a full line
            if not cleared:
                cleared = True
                continue

            # parse the line, output result
            lecture = int(line)

            if args["--raw"]:
                print(lecture)
            else:
                print(format % (lecture * 5.0 / 1023))

        except usb.core.USBError as ex:
            if args["--verbose"]:
                print('USB read error:', ex)
            break


    if not args["--quiet"]:
        print("Disconnecting from the Trinket.\n")


if __name__ == '__main__':
    args = docopt(__doc__, version="Voltrinket 0.1.2")
    try:
        while True: loop()
    except KeyboardInterrupt:
        print("")
