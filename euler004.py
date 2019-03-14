'''
Problem 4

A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

from euler import is_palindrome

multiples = set()

# Creating the set of all 3-digit multiples.
for factor1 in range(100, 1000):
	# For the second loop, we do not need to search and number lower
	# than the number we're currently on in the first loop. We have already
	# multiplied those two in a previous loop.
	# E.g. when factor1 = 102, we do not need to multiply it by factor2 = 101
	# because when factor1 = 101, there was an interation when factor2 = 102.
	# 102 * 101 = 101 * 102
    for factor2 in range(factor1, 1000):
        multiples.add(factor1 * factor2)


smallest_multiple = 100 * 100
largest_multiple = 999 * 999
palindromes = set()

# Creating the set of all palindromes.
for number in range(smallest_multiple, largest_multiple):
    if is_palindrome(number) == True:
    	palindromes.add(number)

both = multiples.intersection(palindromes)
answer = max(both)

print(f"the largest palindromic product of two 3-digit numbers is {answer}.")