python_exceptions = [
    "SyntaxError",
    "NameError",
]

try:
    my_exception = python_exceptions[2]
except IndexError as e:
    help(e)
    raise e