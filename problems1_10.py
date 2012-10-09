from math import sqrt, pow
from collections import Counter
from utils import is_palindrome, eratosthenes, sqr, prime_factors

def problem_one():
    sum = 0
    for i in xrange(1, 1000):
        if (i % 3 == 0) or (i % 5 == 0):
            sum += i
    return sum

def problem_two():
    MAX = 4000000
    first = 1
    second = sum_even_terms= 2
    while second < MAX:
        third = first + second
        first = second
        second = third
        if second % 2 == 0:
            sum_even_terms += second
    return sum_even_terms

def problem_three():
    number = 600851475143
    max = sqrt(number)
    max_prime = 2

    for prime in eratosthenes():
        if prime > max:
            return max_prime
        if number % prime == 0:
            max_prime = prime

def problem_four():
    largest_palindrome = 0
    for i in xrange(100, 999):
        for j in xrange (100, 999):
            product = i * j
            if is_palindrome(product) and product > largest_palindrome:
                largest_palindrome = product

    return largest_palindrome

def problem_five():
    c = Counter()
    sum = 1
    for i in xrange(21):
        i_c = Counter(prime_factors(i))
        c = c | i_c
    for k, v in dict(c).iteritems():
        sum *= int(pow(k, v))
    return sum

def problem_six():
    sum_of_squares = 0
    for i in xrange(1, 101):
        sum_of_squares += (i * i)
    square_of_sums = sum(range(1, 101))
    return square_of_sums * square_of_sums - sum_of_squares

def problem_seven():
    count = 0
    for prime in eratosthenes():
        count += 1
        if count == 10001:
            return prime

def problem_eight(number, consecutive_digits):
    max_product = 0
    string = str(number)
    for i in xrange(0, len(string)-consecutive_digits+1):
        product = 1
        for j in xrange(consecutive_digits):
            product *= int(string[i+j])
        if product > max_product:
            max_product = product
    return max_product

def problem_nine():
    c = 0
    while True:
        c += 1
        for i in xrange(0, c):
            for j in xrange(0, c):
                if i < j and sqr(i) + sqr (j) == sqr(c):
                    if i + j + c == 1000:
                        return i*j*c

def problem_ten():
    MAX = 2000000
    sum = 0
    for prime in eratosthenes():
        if prime < MAX:
            sum += prime
        else:
            return sum
