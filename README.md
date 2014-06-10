# Voltrinket

This is a little project that turns your [Trinket][] into a handy voltimeter.  
It constantly measures and reports the voltage on pin `#2` to the computer.

Use it with a 5V Trinket, otherwise it won't work.

**Important:** Make sure the voltage at the pin doesn't go over 5V, otherwise you
might fry your poor Trinket. I take no responsability for damage occuring to your
Trinket by using this program.

This is based off [TrinketFakeUsbSerial][] which is [explained][fake-usb]
in Adafruit Learning System.


## Install

You should have Python and PIP installed.  
On Debian-based OSes, you can do:

    sudo apt-get install python-pip

Then install the [PyUSB][] and [docopt][] Python modules:

    sudo pip install pyusb docopt

Now go on and [use it](#use)!


## Use

Upload the `voltrinket.ino` sketch to your 5V Trinket.

Then, when the Trinket boots the sketch, run the python script:

    python voltrinket.py

If everything goes well, it'll detect the Trinket and start
displaying voltage lectures from pin `#2` at the console.

You can see which options it accepts with:

    python voltrinket.py --help


## Troubleshooting

TODO: 16MHz, permissions, pin connected well, USB cable correct



[Trinket]: http://learn.adafruit.com/introducing-trinket "The Adafruit Trinket"
[TrinketFakeUsbSerial]: https://github.com/adafruit/Adafruit-Trinket-USB
[fake-usb]: http://learn.adafruit.com/trinket-fake-usb-serial "Trinket Fake USB serial"

[PyUSB]: http://sourceforge.net/apps/trac/pyusb
[docopt]: http://docopt.org
