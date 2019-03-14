'''
Problem 5

2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all
of the numbers from 1 to 20?
'''

from euler import lcm

numbers_1_to_20 = [number for number in range(1, 21)]

answer = lcm(numbers_1_to_20)

print(f"The least common multiple of all numbers 1-20 is {answer}.")