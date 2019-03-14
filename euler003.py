'''
Problem 3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

from euler import list_primes_under

target = 600851475143

primes = list_primes_under(int(target ** 0.5))

for prime in reversed(primes):
    if target % prime == 0:
        answer = prime
        break

print(f"The largest prime factor of {target} is {answer}.")