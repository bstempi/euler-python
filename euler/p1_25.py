from framework import Problem


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
    start, end = 1, 4000000
    current_number = start
    previous_number = start
    sum = 0

    while current_number < end:
        if current_number % 2 == 0:
            sum += current_number

        buff = current_number
        current_number += previous_number
        previous_number = buff

    return sum


@Problem(3)
def problem_3():
    number = 600851475143

    def is_prime(x):
        for j in range(int(x ** 0.5), 2 + 1, -1):
            if x % j == 0:
                return False
        return True

    # Step backwards through possible factors
    for i in range(int(number ** 0.5), 2 + 1, -1):
        # Is it a factor?
        if number % i == 0:
            # Ok, it's a factor; is it prime?
            if is_prime(i):
                return i


@Problem(4)
def problem_4():
    largest_palindrome = 1
    for i in range(999, 99, -1):
        for j in range(999, 99, -1):
            prod = i * j

            # is prod a palindrome?
            num_digits = 0
            while 10 ** num_digits <= prod:
                num_digits += 1

            # Ok, we know the number of digits; let's compare each digit
            is_pal = True
            for k in range(0, num_digits // 2 + 1):
                left_digit = prod // 10 **(num_digits - k - 1) % 10
                right_digit = (prod % (10 ** (k + 1))) // (10 ** k)

                if left_digit != right_digit:
                    is_pal = False
                    break

            # If we got this far, we found one
            if is_pal and prod > largest_palindrome:
                largest_palindrome = prod
    return largest_palindrome


@Problem(5)
def problem_5():
    divisor_start, divisor_end = 2, 20
    num = 0

    is_divisible_by_all = False

    while not is_divisible_by_all:
        num += 20
        is_divisible_by_all = True
        for i in range(divisor_start, divisor_end + 1):
            if num % i != 0:
                is_divisible_by_all = False
                break

    return num
