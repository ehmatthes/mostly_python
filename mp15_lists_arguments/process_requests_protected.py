def validate_requests(raw_requests, valid_requests):
    """Validate a sequence of requests."""
    while raw_requests:
        request = raw_requests.pop(0)
        if "bad" not in request:
            valid_requests.append(request)

# Make a list of raw requests, and a list to hold valid requests.
my_raw_requests = [
    'request_0', 'request_1_bad', 'request_2',
    'request_3_bad', 'request_4_bad', 'request_5',
    'request_6', 'request_7_bad', 'request_8',
    'request_9_bad', 'request_10', 'request_11_bad'
]
my_valid_requests = []

# Validate requests, and see what has changed.
validate_requests(my_raw_requests[:], my_valid_requests)

print(f"My raw requests: {my_raw_requests}")
print(f"My valid requests: {my_valid_requests}")