from random import choices
import sys

try:
    length = int(sys.argv[1])
except IndexError:
    length = 6

keycode = choices("0123456789", k=length)
keycode = "".join(keycode)

print(keycode)
