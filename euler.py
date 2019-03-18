def introot(n):
    return int(int(n) ** 0.5)


def factorial(n):
    n = int(n)
    if n < 0:
        raise ValueError("factorial() received a negative number.")

    if n == 0 or n == 1:
        return 1

    return n * factorial(n-1)


def fibonacci(n):
    # Return the nth Fibonacci number
    if n < 1:
        raise ValueError("fibonacci() received a number less than 1.")

    if n == 1 or n == 2:
        return 1

    return fibonacci(n-2) + fibonacci(n-1)


def list_fibonacci(n, max=0):
    # Returns a list of the first n Fibonacci numbers. If a max value is chosen,
    # this function returns only the Fibonacci numbers below the max value.
    if n < 1:
        raise ValueError("list_fibonacci() received an 'n' less than 1. \
                         'n' is the number of Fibonacci numbers to return.")
    if max != 0 and max < 1:
        raise ValueError("list_fibonacci() received a max Fibonacci value less than 1.")

    fiblist = []
    for num in range(1, n+1):
        if num == 1 or num == 2:
            fiblist.append(1)
        else:
            # Add the two preceding numbers
            newnum = fiblist[-2] + fiblist[-1]
            # Check that we don't stop early
            if max > 0 and newnum > max:
                return fiblist
            fiblist.append(newnum)

    return fiblist



def is_prime(n):
    if n < 2:
        return False

    for number in range(2, introot(n)+1):
        if n % number == 0:
            return False    
    
    return True


def list_primes(n):
    # Returns a list of the first n primes
    if n < 1:
        raise ValueError("list_primes() received an 'n' less than 1. \
                         'n' is the number of primes to return.")

    primes = [2]
    while len(primes) < n:
        # Range start: the number 1 greater than the most recently found prime
        # Range stop: Bertrand's postulate guarantees a prime between n and 2n
        for number in range(primes[-1]+1, 2*(primes[-1]+1)+1):
            isprime = True # Assume the number is prime
            for knownprime in primes: # Compare to each known prime
                if number % knownprime == 0:
                    isprime = False # Proven wrong
                    break

            if isprime == True: # We have proven by exhaustion the number is prime
                primes.append(number)
                if len(primes) == n: # If we just added the nth prime, we're done
                    return primes

    return primes


def list_primes_under(max):
    # Returns a list of all primes under the chosen value
    # Using Sieve of Eratosthenes
    if max < 2:
        raise ValueError("list_primes_under() received a 'max' of less than 2. \
                         'max' is the max size of primes to return.")
    if max == 2:
        return [2]

    primes = []
    composites = set() # Searching sets is O(1), much better than O(n) for lists

    for number in range(2, max):
        if number not in composites:
            # The number is prime. Add it to primes
            primes.append(number)
            # Starting with itself * 2, add each multiple to the composites set
            for multiple in range(number*2, max, number):
                composites.add(multiple)

    return primes


def is_palindrome(n):
    # Boolean to see if the number is a palindrome (e.g. 7, 121, 845548)
    n = abs(n)
    string = str(n)

    if len(string) == 1:
        return True

    # The range is the first half of the digits, int() rounds down
    for digit in range(int(len(string)/2)):
        if string[digit] != string[-1-digit]:
            return False

    return True


def prime_factorize(n):
    # Returns a list of the prime factors of a number
    # Retains -1 as a factor
    try:
        divide_me = n
        factors = []
        if divide_me < 0:
            divide_me = abs(divide_me)
            factors.append(-1)

        # Here divide_me+1 guarantees the correct value even for prime inputs,
        # but then we iterate needlessly over a few primes below. There should 
        # be a way to pass a smaller argument to list_primes_under, but I
        # haven't found it yet.
        primes = list_primes_under(divide_me+1)
        for prime in primes:
            while divide_me % prime == 0:
                factors.append(prime)
                divide_me = divide_me / prime

        return factors

    except ValueError:
        others = set([0, 1, -1])
        if n in others:
            return [n]

        return ValueError("prime_factorize() received a number it can't handle, \
                           likely a non-integer.")


def lcm_two(n1, n2):
    # Returns the least common multiple of two inputs
    list1 = prime_factorize(n1)
    list2 = prime_factorize(n2)
    factordict = {}

    # Add each factor and n1's count to the dictionary
    for factor in set(list1):
        factordict[factor] = list1.count(factor)

    for factor in set(list2):
        # If the factor isn't already there, add it and n2's count
        if factor not in factordict:
            factordict[factor] = list2.count(factor)
        # If it's already there, replace n1's count if n2's count is bigger
        if list2.count(factor) > factordict[factor]:
            factordict[factor] = list2.count(factor)

    lcm = 1
    for prime, exponent in factordict.items():
        lcm *= int(prime) ** int(exponent)

    return lcm


def lcm(list_of_numbers):
    # Returns the least common multiple of all numbers in a list of any size

    # Peel off the first two and do LCM
    peel = lcm_two(list_of_numbers[0], list_of_numbers[1])

    # If these were the only two, we're done
    if len(list_of_numbers) == 2:
        return peel

    # Recursive: pass one fewer argument to lcm()
    newlist = list_of_numbers[2:]
    newlist.append(peel)
    return lcm(newlist)

# Two functions included in euler006.py: sum_of_squares() and square_of_sum()

def string_multiplier(string_of_digits):
    # Multiply each digit in a string
    factors = [int(number) for number in string_of_digits]
    product = 1
    for factor in factors:
        product *= factor

    return product

def list_factors(n):
    # Returns a list of all factors of a number
    # If a number is a factor, it only gets listed once
    # Retains -1
    if n == 0 or n == 1:
        return [n]

    factors = []
    if n < 0:
        factors.append(-1)

    # Here we only check numbers up to its square root
    for integer in range(1, introot(abs(n))):
        if n % integer == 0:
            factors.append(integer)
            factors.append(int(n/integer))

    return factors

def is_pythag(a, b, c):
    # Boolean to see if three integers constitute a Pythagorean triple
    integers = sorted([a, b, c])
    if integers[0] ** 2 + integers[1] ** 2 == integers[2] ** 2:
        return True

    return False


def find_triple_that_sums(n):
    # Find the first Pythagorean triple that sums to n

    # Range start: The smallest any side could be is equal to the others
    # Range stop: The largest side of a triange is less than the sum of the others
    for side1 in range(int(n/3), int(n/2)):
        # Cut the remaining amount of n into two equal parts
        # side2 will always be the smaller part, so only cover the first half
        for side2 in range(1, int((n - side1)/2)):
            # side3 is whatever amound of n is left
            side3 = n - side1 - side2
            if is_pythag(side1, side2, side3):
                return [side1, side2, side3]

    print (f"No triples found that sum to {n}")
    return [0, 0, 0]


def list_triangulars(n):
    # Returns a list of triangular numbers under a certain value
    triangulars = [1]

    for term in range(2, n):
        triangulars.append(triangulars[term-2] + term)

    return triangulars

# Reusable non-function code for matrix operations included in euler011.py

def collatz(n):
    # Return one iteration of the Collatz recursive function
    if n < 2:
        raise ValueError("collatz() received a number less than 2.")
    if n % 2 == 0:
        return int(n/2)
    return 3 * n + 1

def longest_collatz_under(n):
    # Runs the Collatz function on each number under n
    # Returns the n that produced the longest chain AND the length of the chain
    if n < 2:
        raise ValueError("longest_collatz_under() received a number less than 2.")

    record = 0
    record_holder = 0
    for number in range(1, n): 
        chain = 0
        collatz_me = number
        while collatz_me != 1:
            collatz_me = collatz(collatz_me)
            chain += 1

        if chain > record:
            record = chain
            record_holder = number

    return (record_holder, record)