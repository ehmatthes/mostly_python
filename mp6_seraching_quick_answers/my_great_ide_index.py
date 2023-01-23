lines = [
    '"""A simple Hello World program."""',
    "",
    'msg = "Hello Python world!"',
    'print(msg)'        
]

for i in range(len(lines)):
    line_num = i + 1
    print(f"{line_num}\t{lines[i]}")