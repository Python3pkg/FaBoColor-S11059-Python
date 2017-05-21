# coding: utf-8
## @package FaBoColor_S11059
#  This is a library for the FaBo Color I2C Brick.
#
#  http://fabo.io/203.html
#
#  Released under APACHE LICENSE, VERSION 2.0
#
#  http://www.apache.org/licenses/
#
#  FaBo <info@fabo.io>

import FaBoColor_S11059
import time
import sys

s11059 = FaBoColor_S11059.S11059()

try:
    while True:

        color = s11059.read()
        print("r =", (color['r']), end=' ')
        print(" g =", (color['g']), end=' ')
        print(" B =", (color['b']), end=' ')
        print(" ir =", (color['ir']))
        print()
        time.sleep(1)
except KeyboardInterrupt:
    sys.exit()
