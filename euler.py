from math import sqrt, factorial, pow
from collections import Counter

# Helpers

# http://code.activestate.com/recipes/117119/
def eratosthenes():
    '''Yields the sequence of prime numbers via the Sieve of Eratosthenes.'''
    D = {}  # map composite integers to primes witnessing their compositeness
    q = 2   # first integer to test for primality
    while 1:
        if q not in D:
            yield q        # not marked composite, must be prime
            D[q*q] = [q]   # first multiple of q not already marked
        else:
            for p in D[q]: # move each witness to its next multiple
                D.setdefault(p+q,[]).append(p)
            del D[q]       # no longer need D[q], free memory
        q += 1

def prime_factors(n):
    "Returns all the prime factors of a positive integer"
    factors = []
    d = 2
    while (n > 1):
        while (n%d==0):
            factors.append(d)
            n /= d
        d = d + 1

    return factors

def sqr(num):
    return num * num

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

def is_palindrome(obj):
    string = str(obj)
    half_length = len(string)/2
    for i in xrange(half_length):
        if string[i] != string[-1-i]:
            return False
    return True

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
        print k, v
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
        if (count == 10001):
            return prime

def problem_eight(number, consecutive_digits):
    print number
    max_product = 0
    string = str(number)
    print string
    for i in xrange(0, len(string)-consecutive_digits+1):
        product = 1
        for j in xrange(consecutive_digits):
            product *= int(string[i+j])
        if product > max_product:
            max_product = product

    return max_product

def problem_nine():
    c = 0
    while(True):
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

def problem_eleven():
    pass

def hailstorm(number):
    seq = 1
    while number > 1:
        if number % 2 == 0:
            number /= 2
        else:
            number = 3 * number + 1
        seq += 1
    return seq

def problem_fourteen():
    MAX = 1000000
    longest = 0
    starting_longest = 0
    for i in xrange(1, MAX):
        len = hailstorm(i)
        if len > longest:
            print 'new longest ' + str(i)
            longest = len
            starting_longest = i

    return starting_longest


def problem_sixteen():
    string = str(long(pow(2, 1000)))
    sum = 0
    for i in xrange(len(string)):
        sum += int(string[i])
    return sum

def problem_twenty(number):
    fac = factorial(number)
    string = str(fac)
    sum = 0
    for i in xrange(len(string)):
        sum += int(string[i])
    return sum

def problem_twenty_five(num_digits):
    first = 1
    second = 1
    terms = 2
    while True:
        third = first + second
        first = second
        second = third
        terms += 1
        if num_digits == len(str(second)):
            return terms


def is_curious(num):
    string = str(num)
    sum = 0
    for i in xrange(len(string)):
        sum += factorial(int(string[i]))
    return sum == num

def problem_thirty_four():
    MAX = 1000000
    sum = 0
    for i in xrange(3, MAX):
        if is_curious(i):
            sum += i
    return sum


def problem_thirty_six():
    sum = 0
    for i in xrange(1000000):
        if (is_palindrome(str(i))) and is_palindrome(str(bin(i))[2:]):
            sum += i
    return sum


def problem_forty_eight():
    sum = 0
    for i in xrange(1, 1001):
        sum += long(i) ** long(i)
    return str(sum)[-10:]

if __name__=="__main__":
    print  'solving'
    answer = problem_five()
    print answer
    print 'done!'


