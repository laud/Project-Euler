from math import sqrt, factorial

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

def triangle():
    current = 1
    sum = 0
    while 1:
        sum += current
        current += 1
        yield sum

def prime_factors(n):
    "Returns all the prime factors of a positive integer"
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n /= d
        d += 1

    return factors

def sqr(num):
    return num * num

def is_palindrome(obj):
    string = str(obj)
    half_length = len(string)/2
    for i in xrange(half_length):
        if string[i] != string[-1-i]:
            return False
    return True

def factors(to_factor):
    """Find the factors of to_factor."""
    factors = []
    divisor = 1
    while divisor <= int(sqrt(to_factor)):
        if not to_factor % divisor:
            quotient = to_factor / divisor
            factors.append(divisor)
            factors.append(quotient)
        divisor += 1

    return factors

def memoize(f):
    cache= {}
    def memf(*x):
        if x not in cache:
            cache[x] = f(*x)
        return cache[x]
    return memf
