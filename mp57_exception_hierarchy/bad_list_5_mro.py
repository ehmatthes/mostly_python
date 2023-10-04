python_exceptions = [
    "SyntaxError",
    "NameError",
]

try:
    my_exception = python_exceptions[2]
except LookupError as e:
    print(type(e).mro())
    raise e