'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

from euler import find_triple_that_sums

triple = find_triple_that_sums(1000)

answer = triple[0] * triple[1] * triple[2]

print(f"The product of a, b, and c for the Pythagorean triple that adds to 1000 is {answer}.")