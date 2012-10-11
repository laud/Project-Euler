from math import factorial, pow
from utils import triangle, factors, memoize

def problem_eleven(num_consecutive):
    grid = []
    file = open('problem_files/problem11.txt')
    for line in file:
        grid.append(line.split())
    height = len(grid)
    width = len(grid[0]) if height > 0 else 0
    max_product = 0

    # Check horizontal
    for i in xrange(0, height):
        for j in xrange(0, width-num_consecutive+1):
            product = 1
            for k in xrange(num_consecutive):
                product *= int(grid[i][j+k])
            if product > max_product:
                max_product = product

    # Check vertical
    for i in xrange(0, width):
        for j in xrange(0, height-num_consecutive+1):
            product = 1
            for k in xrange(num_consecutive):
                product *= int(grid[j+k][i])
            if product > max_product:
                max_product = product

    # Check diagonals going down
    for i in xrange(0, height-num_consecutive+1):
        for j in xrange(0, width-num_consecutive+1):
            product = 1
            for k in xrange(num_consecutive):
                product *= int(grid[i+k][j+k])
            if product > max_product:
                max_product = product

    # Check diagonals going up
    for i in xrange(num_consecutive-1, height):
        for j in xrange(0, width-num_consecutive+1):
            product = 1
            for k in xrange(num_consecutive):
                product *= int(grid[i-k][j+k])
            if product > max_product:
                max_product = product

    return max_product

def problem_twelve():
    for tri in triangle():
        num_divisors = len(factors(tri))
        print tri, num_divisors
        if num_divisors > 500:
            return tri

def problem_thirteen():
    sum = 0
    file = open('problem_files/problem13.txt')
    for line in file:
        sum += long(line)
    return str(sum)[:10]

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
            longest = len
            starting_longest = i

    return starting_longest

@memoize
def find_route(right, down):
#    print right, down
    if right == 0 and down == 0:
        return 1
    paths = 0
    if right > 0:
        paths += find_route(right-1, down)
    if down > 0:
        paths += find_route(right, down-1)
    return paths

def problem_fifteen():
    return find_route(20, 20)
#    return factorial(40)/ (factorial(20)*factorial(40-20))

def problem_sixteen():
    string = str(long(pow(2, 1000)))
    sum = 0
    for i in xrange(len(string)):
        sum += int(string[i])
    return sum


def num_to_string(num):
    single = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    double = ['ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    teens = ['eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    hundred = 'hundred'
    thousand = 'thousand'


    str = ''
    if num / 1000 > 0:
        str += single[num/1000-1] + thousand
        num %= 1000
    if num / 100 > 0:
        str += single[num/100-1] + hundred
        num %= 100
    if len(str) > 0 and num > 0:
        str += 'and'
    if num / 10 > 0:
        if num > 10 and num < 20:
            str += teens[num-10-1]
            return str
        else:
            str += double[num/10-1]
        num %= 10
    if num > 0:
        str += single[num-1]
    return str


def string_strip_all_length(str):
    return len(str.replace(' ', ''))

def problem_seventeen():
    sum = 0
    for i in xrange(1, 1001):
        str = num_to_string(i)
        sum += string_strip_all_length(str)
        print str
    return sum

def problem_eighteen():
    tree = []
    with open('problem_files/problem18.txt') as f:
        for l in f:
            tree.append(l.split())

    for i in xrange(len(tree)-2, -1, -1):
        for j in xrange(0, len(tree[i])):
            tree[i][j] = int(tree[i][j]) + int(max(tree[i+1][j], tree[i+1][j+1]))

    return tree[0][0]

def problem_twenty(number):
    fac = factorial(number)
    string = str(fac)
    sum = 0
    for i in xrange(len(string)):
        sum += int(string[i])
    return sum
