from random import choice

requests = []
for r_num in range(12):
    request = f"request_{r_num}"
    if choice([True, False]):
        request += "_bad"
    requests.append(request)

print(requests)