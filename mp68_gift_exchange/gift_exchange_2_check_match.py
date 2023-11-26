names = [
    "Sherri",
    "Eric",
    "Terri",
    "Joel",
    "Joshua",
    "Catherine",
    "Jasmine",
    "Alexandra",
    "Jeremiah",
]

partners = [
    ("Sherri", "Eric"),
    ("Terri", "Joel"),
    ("Joshua", "Catherine"),
    ("Jasmine", "Alexandra"),
]

def check_match(match):
    if match in partners:
        return False
    if tuple(reversed(match)) in partners:
        return False
    return True

print(check_match(('Sherri', 'Eric')))
print(check_match(('Eric', 'Sherri')))
print(check_match(('Sherri', 'Terri')))