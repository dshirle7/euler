'''
Problem 6
The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of
the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of
the first one hundred natural numbers and the square of the sum.
'''

numbers_1_to_100 = [number for number in range(1, 101)]

def sum_of_squares(list_of_numbers):
    # Returns the sum of the squares of all numbers in a list of any size
    squares = [number ** 2 for number in list_of_numbers]
    return sum(squares)

def square_of_sum(list_of_numbers):
    # Returns the square of the sum of all numbers in a list of any size
    return(sum(list_of_numbers) ** 2)

lower = sum_of_squares(numbers_1_to_100)
upper = square_of_sum(numbers_1_to_100)

answer = upper - lower

print(f"The difference between the sum of the squares of the first \
	    one hundred natural numbers and the square of the sum is {answer}.")