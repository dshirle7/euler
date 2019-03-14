'''
Problem 7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''

from euler import list_primes

list_of_primes = list_primes(10001)

answer = list_of_primes[-1]

print(f"The 10,001st prime number is {answer}.")