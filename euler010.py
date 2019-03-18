'''
Problem 10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

from euler import list_primes_under

primes = list_primes_under(2000000)

answer = sum(primes)

print(f"The sum of all the primes below two million is {answer}.")