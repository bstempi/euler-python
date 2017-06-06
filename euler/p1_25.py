from framework import Problem


@Problem(1)
def problem_1():
    """
    Simple solution; I iterate from 1 to 1000 (inc) and test to see if it's divisible by 3 or 5, adding the value to a
    running total if it is.
    :return:
    """
    start, end = 1, 1000
    sum = 0

    for i in range(start, end):
        if i % 3 == 0 or i % 5 == 0:
            sum += i

    return sum


@Problem(2)
def problem_2():
    """
    A running sum and a buffer of the previous value is used to generate a Fib sequence.  Each number of the sequence
    is tested to see if its even.  If it is, it is added to a running sum.
    :return:
    """
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
    """
    Knowing that the largest number that will divide into x is x^0.5 (because x^0.5 * x^0.5 = x), I start at x^0.5
    (promounced, "root of x") and count backwards to 2, testing each number to see if it divides evenly into our target.
    If it does, I test to see if it's prime using brute force plus the root-x optimization.
    :return:
    """
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
    """
    This problem is a pain because the formula to get the first/last digits can be tricky.  I did it by using a
    combination of dividing by multiples 10 to drop digits and using modulous by multiples of 10 to get a single digit.
    The intuition is that by combining these two operations, I can write formulas that return a given digit.
    :return:
    """
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
    """
    This solution generates numbers that are multiples of 20 and tests to see if the range from 2 to 20, inc, will divide
    into it.  The intuition here is that since 20 is the largest factor, using it as a stepping value will help us
    eliminate lots of values that wouldn't work.
    :return:
    """
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


@Problem(6)
def problem_6():
    """
    This is one of those problems that's hard because it's a work problem and the word order is confusing.  The solution
    is really simple and only involves a single loop and two counters.
    :return:
    """
    start, end = 1, 100

    sum_of_squares = 0
    sum_of_numbers = 0

    for i in range(start, end + 1):
        sum_of_numbers += i
        sum_of_squares += i ** 2

    square_of_sum = sum_of_numbers ** 2

    return square_of_sum - sum_of_squares


@Problem(7)
def problem_7():
    """
    This problem is brute-force-ish. It tests if a number is prime by trying to divide every number between 2 and root-x
    into it.  If it's prime, we increment a counter.  Once our counter has hit a certain value, we return x.
    :return:
    """
    primes_found = 0
    current_num = 2

    while True:
        # Is it prime?
        is_prime = True
        for i in range(2, int(current_num ** 0.5) + 1):
            if i != current_num and current_num % i == 0:
                is_prime = False
                break

        if is_prime:
            primes_found += 1
        if primes_found == 10001:
            return current_num

        current_num += 1


@Problem(8)
def problem_8():
    """
    I solved this problem by treating the number as a string and calling the `range()` function in a loop to get given
    chunk.  I then iterated over every character, cast it to an int, and multiplied it to some running value, which would
    get compared to the globally greatest product.

    We could take this as number and use a combination of integer division and modulo on it, but this is a ridiculously
    large number, so I'll leave that for some other exercise.
    :return:
    """
    really_long_number = '7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450'
    greatest_product = 0

    for i in range(0, len(really_long_number) - 13 + 1):
        subset = really_long_number[i:i+13]
        product = 1
        for char in subset:
            product *= int(char)

        if product > greatest_product:
            greatest_product = product

    return greatest_product


@Problem(9)
def problem_9():
    """
    Brute force; not optimal but runs in a few seconds.  I run through all iterations of a, b, c, each from 1 to 1000,
    inc, and test it's sum.  If it's sum matches our target, I test to see if it's a Py triplet.
    :return:
    """
    target_sum = 1000

    for a in range(1, 1001):
        for b in range(1, 1001):
            for c in range(1, 1001):
                if a + b + c == target_sum:
                    if a ** 2 + b ** 2 == c ** 2:
                        return a * b * c


@Problem(10)
def problem_10():
    """
    This problem brute-forces prime testing using the root-x optimization for every number between 2 and 2000000 while
    keeping a running total.
    :return:
    """
    highest_prime = 2000000
    sum = 0

    def is_prime(x):
        for j in range(2, int(x ** 0.5) + 1):
            if x % j == 0:
                return False
        return True

    for i in range(2, highest_prime):
        if is_prime(i):
            sum += i

    return sum


@Problem(11)
def problem_11():
    """
    This answer isn't anything special; it's just a bunch of index arithmetic.
    :return:
    """
    grid = [
        [8, 2, 22, 97, 38, 15, 0, 40, 0, 75, 4, 5, 7, 78, 52, 12, 50, 77, 91, 8],
        [49, 49, 99, 40, 17, 81, 18, 57, 60, 87, 17, 40, 98, 43, 69, 48, 4, 56, 62, 0],
        [81, 49, 31, 73, 55, 79, 14, 29, 93, 71, 40, 67, 53, 88, 30, 3, 49, 13, 36, 65],
        [52, 70, 95, 23, 4, 60, 11, 42, 69, 24, 68, 56, 1, 32, 56, 71, 37, 2, 36, 91],
        [22, 31, 16, 71, 51, 67, 63, 89, 41, 92, 36, 54, 22, 40, 40, 28, 66, 33, 13, 80],
        [24, 47, 32, 60, 99, 3, 45, 2, 44, 75, 33, 53, 78, 36, 84, 20, 35, 17, 12, 50],
        [32, 98, 81, 28, 64, 23, 67, 10, 26, 38, 40, 67, 59, 54, 70, 66, 18, 38, 64, 70],
        [67, 26, 20, 68, 2, 62, 12, 20, 95, 63, 94, 39, 63, 8, 40, 91, 66, 49, 94, 21],
        [24, 55, 58, 5, 66, 73, 99, 26, 97, 17, 78, 78, 96, 83, 14, 88, 34, 89, 63, 72],
        [21, 36, 23, 9, 75, 0, 76, 44, 20, 45, 35, 14, 0, 61, 33, 97, 34, 31, 33, 95],
        [78, 17, 53, 28, 22, 75, 31, 67, 15, 94, 3, 80, 4, 62, 16, 14, 9, 53, 56, 92],
        [16, 39, 5, 42, 96, 35, 31, 47, 55, 58, 88, 24, 0, 17, 54, 24, 36, 29, 85, 57],
        [86, 56, 0, 48, 35, 71, 89, 7, 5, 44, 44, 37, 44, 60, 21, 58, 51, 54, 17, 58],
        [19, 80, 81, 68, 5, 94, 47, 69, 28, 73, 92, 13, 86, 52, 17, 77, 4, 89, 55, 40],
        [4, 52, 8, 83, 97, 35, 99, 16, 7, 97, 57, 32, 16, 26, 26, 79, 33, 27, 98, 66],
        [88, 36, 68, 87, 57, 62, 20, 72, 3, 46, 33, 67, 46, 55, 12, 32, 63, 93, 53, 69],
        [4, 42, 16, 73, 38, 25, 39, 11, 24, 94, 72, 18, 8, 46, 29, 32, 40, 62, 76, 36],
        [20, 69, 36, 41, 72, 30, 23, 88, 34, 62, 99, 69, 82, 67, 59, 85, 74, 4, 36, 16],
        [20, 73, 35, 29, 78, 31, 90, 1, 74, 31, 49, 71, 48, 86, 81, 16, 23, 57, 5, 54],
        [1, 70, 54, 71, 83, 51, 54, 69, 16, 92, 33, 48, 61, 43, 52, 1, 89, 19, 67, 48],
    ]

    greatest_product = 0
    series_length = 4

    # Test all numbers that are horizontally adjacent
    for line in grid:
        for start_i in range(0, len(grid[0]) - series_length):
            series = line[start_i:start_i + series_length]
            current_product = 1
            for num in series:
                current_product *= num

            if current_product > greatest_product:
                greatest_product = current_product

    # Test all numbers that are vertically adjacent
    for col_index in range(0, len(grid[0])):
        for line_index in range(0, len(grid) - series_length):
            current_product = 1
            for offset in range(0, series_length):
                current_product *= grid[col_index][line_index + offset]

                if current_product > greatest_product:
                    greatest_product = current_product

    # Test all diagonal numbers down, right
    for col_index in range(0, len(grid[0]) - series_length):
        for line_index in range(0, len(grid) - series_length):
            current_product = 1
            for offset in range(0, series_length):
                current_product *= grid[col_index + offset][line_index + offset]

                if current_product > greatest_product:
                    greatest_product = current_product

    # Test all diagonal numbers down, left
    for col_index in range(series_length - 1, len(grid[0])):
        for line_index in range(0, len(grid) - series_length):
            current_product = 1
            for offset in range(0, series_length):
                current_product *= grid[col_index - offset][line_index + offset]

                if current_product > greatest_product:
                    greatest_product = current_product

    return greatest_product