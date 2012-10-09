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