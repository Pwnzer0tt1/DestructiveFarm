#!/usr/bin/env python3

import random
import sys

print("Hello! I am a little sploit. I could be written on any language, but "
      "my author loves Python. Look at my source - it is really simple. "
      "I should steal flags and print them on stdout or stderr. ")

print("My args are: %s" % sys.argv)

print("Here are some random flags for you:")

print("First flag is %031d=" % random.randrange(0, 10000))
print("Second flag is %031d=" % random.randrange(0, 10000))
