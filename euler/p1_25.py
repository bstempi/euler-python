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
