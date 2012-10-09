from math import factorial
from utils import is_palindrome

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
