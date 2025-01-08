from random import choices
import sys

try:
    length = int(sys.argv[1])
except IndexError:
    length = 6

while True:
    keycode = choices("0123456789", k=length)
    if len(set(keycode)) == length - 1:
        break    

keycode = "".join(keycode)
print(keycode)
