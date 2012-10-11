from utils import factors

def sum_proper_divisors(n):
    return sum(factors(n))-n

def problem_twenty_one():
    amicable_numbers = set()
    for i in xrange(1, 10000):
        divisor_sum = sum_proper_divisors(i)
        if i != divisor_sum and i == sum_proper_divisors(divisor_sum):
            print i, divisor_sum
            amicable_numbers.add(i)
            amicable_numbers.add(divisor_sum)
    print sum(list(amicable_numbers))

def calculate_alphabetical_value(str):
    str = str.lower()
    sum = 0
    for i in xrange(len(str)):
        sum += ord(str[i]) - ord('a') + 1
    return sum

def problem_twenty_two():
    names = []
    with open('problem22.txt') as f:
        for l in f:
            names = sorted(map(lambda str: str[1:-1], l.rsplit(',')))

    name_score = 0
    for i in xrange(len(names)):
        value = calculate_alphabetical_value(names[i])
        name_score += (i+1) * value

    return name_score

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