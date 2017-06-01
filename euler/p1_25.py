from euler.framework import Problem


@Problem(1)
def problem_1():
    start, end = 1, 1000
    sum = 0

    for i in range(start, end):
        if i % 3 == 0 or i % 5 == 0:
            sum += i

    return sum



@Problem(2)
def problem_2():
    pass


@Problem(3)
def problem_3():
    pass


@Problem(4)
def problem_4():
    pass


@Problem(5)
def problem_5():
    pass