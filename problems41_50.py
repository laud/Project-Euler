def problem_forty_eight():
    sum = 0
    for i in xrange(1, 1001):
        sum += long(i) ** long(i)
    return str(sum)[-10:]