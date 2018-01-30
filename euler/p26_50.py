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
