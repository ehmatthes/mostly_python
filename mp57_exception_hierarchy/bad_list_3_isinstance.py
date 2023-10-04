python_exceptions = [
    "SyntaxError",
    "NameError",
]

try:    
    my_exception = python_exceptions[2]
except IndexError as e:
    print(isinstance(e, LookupError))
    raise e