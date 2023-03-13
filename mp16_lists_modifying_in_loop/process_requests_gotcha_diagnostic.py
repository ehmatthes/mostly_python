# process_requests_gotcha.py

# Make a mix of valid and invalid requests.
requests = [
    'request_0', 'request_1_bad', 'request_2',
    'request_3_bad', 'request_4_bad', 'request_5',
    'request_6', 'request_7_bad', 'request_8',
    'request_9_bad', 'request_10', 'request_11_bad'
]

# Remove invalid requests.
for index, request in enumerate(requests):
    print(f"Examining request: {index} - {request}")
    if 'bad' in request:
        requests.remove(request)

# Show what's left.
print(requests)