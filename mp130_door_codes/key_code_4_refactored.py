from random import choices
import sys

try:
    length = int(sys.argv[1])
except IndexError:
    length = 6

def get_keycode():
    """Generate a reasonably secure keycode."""
    while True:
        keycode = choices("0123456789", k=length)
        if len(set(keycode)) == length - 1:
            return "".join(keycode)    

keycode = get_keycode()
print(keycode)
