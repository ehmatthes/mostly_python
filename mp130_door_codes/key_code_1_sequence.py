from random import choices

keycode = choices("0123456789", k=6)
keycode = "".join(keycode)

print(keycode)
