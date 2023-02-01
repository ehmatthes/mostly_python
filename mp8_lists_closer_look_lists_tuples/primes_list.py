primes = [2, 3, 5, 7, 11]
primes_id = id(primes)
print(primes_id, primes)

primes.append(13)
primes_id = id(primes)
print(primes_id, primes)