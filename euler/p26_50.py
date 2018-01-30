import itertools
import math

from framework import Problem


@Problem(26)
def problem_26():
    """
    To solve this problem, I had to learn how to turn decimal fractions into binary.  I found this guide:
    https://www.cs.drexel.edu/~introcs/Fa11/notes/07.1_FloatingPoint/repeatingBFalgorithm.html?CurrentSlide=3

    The idea here is that for each number 1 through 999 (inc), I'll treat it like a fraction (1/x) and then use the
    guide above to try to turn it into a decimal.

    The only difference is we'll do it in base 10 instead of base 2

    After processing each fraction, we'll place that fraction and it's position index into a hash map.  If we find that
    fraction again, we'll know that we've hit a repeat and where it started, allowing us to find the length of the
    repeat.
    :return:
    """

    greatest_sequence_len = 0
    greatest_d = 0

    for i in range(1, 1000):
        numerator = 1
        denominator = i

        fraction_map = dict()

        # While we haven't found the end of our decimal...
        # This works because we keep going until there's nothing left to double the size of)
        j = 0
        while numerator > 0:
            #  Step 1:  Multiply the fraction by two
            numerator *= 10

            # Step two:  check if the numerator larger than the denominator?
            flip_bit = numerator >= denominator

            # Step three:  If we flipped our bit, we need to subtract the denom from the neum
            numerator = numerator % denominator if flip_bit else numerator

            # Step 4:  Have we seen this fraction before?  Then we have a repeat
            if (numerator, denominator) in fraction_map:
                current_sequence_len = j - fraction_map[(numerator, denominator)]

                # Step 4.1:  Is this our new longest sequence?
                if current_sequence_len > greatest_sequence_len:
                    greatest_sequence_len = current_sequence_len
                    greatest_d = i

                # No matter what, we found a sequence and therefore need to move on
                break

            # Step 5:  We've not seen this before and we need to log it
            fraction_map[(numerator, denominator)] = j
            j += 1

    return greatest_d


@Problem(27)
def problem_27():
    """
    I'm brute forcing this.  There are a few things to note, however:
    *  We're going to be constantly testing numbers for primality, so we might as well make a set of numbers that are
    prime below a certain number (say, a few million).  As long as the number we're considering isn't larger than the
    last number tested when building the set, we only have to do a set lookup instead of prime factoring.  We'll find
    this value via experimentation.

    * Because we're using such a wide range of numbers, we'll calculate primes differently in this solution than we have
    in others.  We'll use the Sieve of Eratosthenes (https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes)
    :return:
    """

    # Set the limit of the primes we're looking for and create a list where we set them all to prime by default
    prime_upper_limit = 20000
    primes = list(itertools.repeat(True, prime_upper_limit))
    prime_set = set()

    greatest_ns_a = None
    greatest_ns_b = None
    greatest_n = -1

    # Finding primes via https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
    for i in range(2, math.ceil(math.sqrt(prime_upper_limit)) + 1):
        # If we haven't already marked the current number as non-prime, mark all of it's multiples as non-prime
        # Also note the correction for a 0-based list
        if primes[i-1] is True:
            prime_set.add(i)

            for k in range(2, (prime_upper_limit // i) + 1):
                primes[i * k - 1] = False

    # Ok, the outer-loop has evaluated up to sqroot(prime_upper_limit).  To find the primes larger than that, we simply
    # iterate through the bit-list to find elements that are still marked true
    for i in range(math.ceil(math.sqrt(prime_upper_limit)), prime_upper_limit + 1):
        if primes[i-1] is True:
            prime_set.add(i)

    # Ok, now here's where we test all of our combinations of a and b
    for a in range(-1000, 1000 + 1, 1):
        for b in range(-1000, 1000 + 1, 1):
            # Using our optimization from our function doc:  is b prime?
            if math.fabs(b) not in prime_set:
                continue

            # n starts at 0 and goes until a break is hit
            for n in itertools.count(0):
                x = n**2 + (a * n) + b

                # Our safeguard against our prime list being too small
                if x > prime_upper_limit:
                    raise Exception('The numbers being tested are larger than our pre-generated prime set')

                # Our exit condition for considering this a, b combination
                if x not in prime_set:
                    if n - 1 > greatest_n:
                        greatest_ns_a = a
                        greatest_ns_b = b
                        greatest_n = n - 1
                    break

    return greatest_ns_a * greatest_ns_b
