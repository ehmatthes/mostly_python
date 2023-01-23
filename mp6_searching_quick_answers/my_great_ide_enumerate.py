lines = [
    '"""A simple Hello World program."""',
    "",
    'msg = "Hello Python world!"',
    'print(msg)'        
]

for index, line in enumerate(lines):
    line_num = index + 1
    print(f"{line_num}\t{line}")