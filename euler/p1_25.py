import itertools
import math

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


@Problem(12)
def problem_12():
    """
    The factor calculation is the same as the other prime calculations I've done:  brute force with root-x optimization.
    :return:
    """
    target_divisors = 500
    current_triangle_number = 1
    current_triangle_iteration = 1

    while True:
        current_divisor_count = 0
        for i in range(int(current_triangle_number ** 0.5), 0, -1):
            if current_triangle_number % i == 0:
                # If we've found that i is a divisor, so it d/i
                current_divisor_count += 2

                # if i is a divisor, so is x/i, but i and x/i could be the same number...
                if i ** 2 == current_triangle_number:
                    current_divisor_count =- 1

        if current_divisor_count >= target_divisors:
            return current_triangle_number

        # Calculate the next triangle number
        current_triangle_iteration += 1
        current_triangle_number += current_triangle_iteration


@Problem(13)
def problem_13():
    numbers = [
        37107287533902102798797998220837590246510135740250,
        46376937677490009712648124896970078050417018260538,
        74324986199524741059474233309513058123726617309629,
        91942213363574161572522430563301811072406154908250,
        23067588207539346171171980310421047513778063246676,
        89261670696623633820136378418383684178734361726757,
        28112879812849979408065481931592621691275889832738,
        44274228917432520321923589422876796487670272189318,
        47451445736001306439091167216856844588711603153276,
        70386486105843025439939619828917593665686757934951,
        62176457141856560629502157223196586755079324193331,
        64906352462741904929101432445813822663347944758178,
        92575867718337217661963751590579239728245598838407,
        58203565325359399008402633568948830189458628227828,
        80181199384826282014278194139940567587151170094390,
        35398664372827112653829987240784473053190104293586,
        86515506006295864861532075273371959191420517255829,
        71693888707715466499115593487603532921714970056938,
        54370070576826684624621495650076471787294438377604,
        53282654108756828443191190634694037855217779295145,
        36123272525000296071075082563815656710885258350721,
        45876576172410976447339110607218265236877223636045,
        17423706905851860660448207621209813287860733969412,
        81142660418086830619328460811191061556940512689692,
        51934325451728388641918047049293215058642563049483,
        62467221648435076201727918039944693004732956340691,
        15732444386908125794514089057706229429197107928209,
        55037687525678773091862540744969844508330393682126,
        18336384825330154686196124348767681297534375946515,
        80386287592878490201521685554828717201219257766954,
        78182833757993103614740356856449095527097864797581,
        16726320100436897842553539920931837441497806860984,
        48403098129077791799088218795327364475675590848030,
        87086987551392711854517078544161852424320693150332,
        59959406895756536782107074926966537676326235447210,
        69793950679652694742597709739166693763042633987085,
        41052684708299085211399427365734116182760315001271,
        65378607361501080857009149939512557028198746004375,
        35829035317434717326932123578154982629742552737307,
        94953759765105305946966067683156574377167401875275,
        88902802571733229619176668713819931811048770190271,
        25267680276078003013678680992525463401061632866526,
        36270218540497705585629946580636237993140746255962,
        24074486908231174977792365466257246923322810917141,
        91430288197103288597806669760892938638285025333403,
        34413065578016127815921815005561868836468420090470,
        23053081172816430487623791969842487255036638784583,
        11487696932154902810424020138335124462181441773470,
        63783299490636259666498587618221225225512486764533,
        67720186971698544312419572409913959008952310058822,
        95548255300263520781532296796249481641953868218774,
        76085327132285723110424803456124867697064507995236,
        37774242535411291684276865538926205024910326572967,
        23701913275725675285653248258265463092207058596522,
        29798860272258331913126375147341994889534765745501,
        18495701454879288984856827726077713721403798879715,
        38298203783031473527721580348144513491373226651381,
        34829543829199918180278916522431027392251122869539,
        40957953066405232632538044100059654939159879593635,
        29746152185502371307642255121183693803580388584903,
        41698116222072977186158236678424689157993532961922,
        62467957194401269043877107275048102390895523597457,
        23189706772547915061505504953922979530901129967519,
        86188088225875314529584099251203829009407770775672,
        11306739708304724483816533873502340845647058077308,
        82959174767140363198008187129011875491310547126581,
        97623331044818386269515456334926366572897563400500,
        42846280183517070527831839425882145521227251250327,
        55121603546981200581762165212827652751691296897789,
        32238195734329339946437501907836945765883352399886,
        75506164965184775180738168837861091527357929701337,
        62177842752192623401942399639168044983993173312731,
        32924185707147349566916674687634660915035914677504,
        99518671430235219628894890102423325116913619626622,
        73267460800591547471830798392868535206946944540724,
        76841822524674417161514036427982273348055556214818,
        97142617910342598647204516893989422179826088076852,
        87783646182799346313767754307809363333018982642090,
        10848802521674670883215120185883543223812876952786,
        71329612474782464538636993009049310363619763878039,
        62184073572399794223406235393808339651327408011116,
        66627891981488087797941876876144230030984490851411,
        60661826293682836764744779239180335110989069790714,
        85786944089552990653640447425576083659976645795096,
        66024396409905389607120198219976047599490197230297,
        64913982680032973156037120041377903785566085089252,
        16730939319872750275468906903707539413042652315011,
        94809377245048795150954100921645863754710598436791,
        78639167021187492431995700641917969777599028300699,
        15368713711936614952811305876380278410754449733078,
        40789923115535562561142322423255033685442488917353,
        44889911501440648020369068063960672322193204149535,
        41503128880339536053299340368006977710650566631954,
        81234880673210146739058568557934581403627822703280,
        82616570773948327592232845941706525094512325230608,
        22918802058777319719839450180888072429661980811197,
        77158542502016545090413245809786882778948721859617,
        72107838435069186155435662884062257473692284509516,
        20849603980134001723930671666823555245252804609722,
        53503534226472524250874054075591789781264330331690,
    ]

    sum_of_each_col = list()

    # Calculate the total for each column
    for i in range(0, 50):

        current_sum = 0
        for num in numbers:
            # This bit is dense and has a few subtle bits in it:
            # We first take the number and truncate the digits we don't need on the right.  We do this by dividing it
            # by some multiple of 10 (the math.pow bit).  Also notice that we use // for division.  This returns an int.
            # Using a single slash returns a float and causes incorrect answers.
            # Lastly, we need the last digit.  We get this with the modulous operator.
            digit = (num // int(math.pow(10, i))) % 10
            current_sum += int(digit)

        sum_of_each_col.append(current_sum)

    # Start adding each column together, truncating insignificant digits as we go along
    sum = 0
    digits_to_trim = 0

    for col_index, col_sum in enumerate(sum_of_each_col):
        # the col_index here is the 10's offset
        # to calculate the number we should add, we'd normally to num + (10 * the col offset).
        # We might need to change that offset so that we're not tracking so many digits, so here's where we do that.

        tens_offset = col_index - digits_to_trim
        adjusted_col_sum = col_sum * int(math.pow(10, tens_offset))
        sum = sum + adjusted_col_sum

        # Here's where we need to check that our answer is still under ten digits.  If it's over, we need to truncate
        # and update the digits_to_trim
        sum_digit_count = math.ceil(math.log10(sum))
        if sum_digit_count > 10:
            # How many are we over this time?
            current_answer_digits_over = sum_digit_count - 10
            digits_to_trim += current_answer_digits_over
            sum = sum // int(math.pow(10, current_answer_digits_over))

    return sum


@Problem(14)
def problem_14():
    """
    Unoptimized brute-force approach.
    :return:
    """
    longest_chain_root = 0
    longest_chain_len = 0

    for i in range(2, 1000000 + 1):
        current_chain_len = 1
        current_n = i
        while current_n != 1:
            if current_n % 2 == 0:
                current_n = current_n // 2
            else:
                current_n = current_n * 3 + 1

            current_chain_len += 1

        if current_chain_len > longest_chain_len:
            longest_chain_len = current_chain_len
            longest_chain_root = i

    return longest_chain_root


@Problem(15)
def problem_15():
    """
    This problem is a permutation problem.

    In the example 2 by 2 grid given, there are 6 possible ways to traverse.  No matter how you traverse, you must make
    4 moves; 2 of them must be downs and 2 of them must be rights.  Instead of visualizing the problem as a grid, you
    could visualize it like this:

    (DDRR), (RRDD), (DRDR), (RDRD), etc.  If you remember prob/stat from high school or college, this should look
    familiar.  We can restate the problem:  What are all of the permutations of 2 Ds and 2 Rs?  The formula becomes

    (total number of elements)! / (elements in A !)(elements in B !) etc etc
    See https://en.wikipedia.org/wiki/Permutation#Permutations_with_repetition

    In the case of a 20 by 20 grid, we must make 20 downs and 20 rights, so the formula becomes 40! / (20! * 20!)
    :return:
    """
    return math.factorial(40) // (math.factorial(20) * math.factorial(20))


@Problem(16)
def problem_16():
    """
    This problem is all about writing a function that sums the digits.

    We sum the digits by getting the last digit (modulous 10).  We then truncate the digit by dividing by 10.  Rinse
    and repeat.
    :return:
    """

    num = int(math.pow(2, 1000))
    sum = 0

    while num > 0:
        current_digit = num % 10
        sum += current_digit
        num = num // 10

    return sum


@Problem(17)
def problem_17():
    """
    To solve this problem, I iterate over all of the numbers between 1 and 1000, incl.  I then break down the number
    into it's individual digits and use a series of if statements to determine what words to use.  I keep a dictionary
    that contains a number or word and returns the number of letters in that number/word.  I keep a running tally and
    return it at the end.
    :return:
    """

    char_counts = {
        0: 0,
        1: len('one'),
        2: len('two'),
        3: len('three'),
        4: len('four'),
        5: len('five'),
        6: len('six'),
        7: len('seven'),
        8: len('eight'),
        9: len('nine'),
        10: len('ten'),
        11: len('eleven'),
        12: len('twelve'),
        13: len('thirteen'),
        14: len('fourteen'),
        15: len('fifteen'),
        16: len('sixteen'),
        17: len('seventeen'),
        18: len('eighteen'),
        19: len('nineteen'),
        20: len('twenty'),
        30: len('thirty'),
        40: len('forty'),
        50: len('fifty'),
        60: len('sixty'),
        70: len('seventy'),
        80: len('eighty'),
        90: len('ninety'),
        100: len('hundred'),
        1000: len('thousand'),
        'and': len('and'),
    }
    sum = 0

    for i in range(1, 1000 + 1):
        # First step:  Break the number down into it's components:
        ones_place = i % 10
        tens_place = (i % 100) // 10
        hundreds_place = (i % 1000) // 100
        thousands_place = (i % 10000) // 1000

        # Next, we form our counts by going from the thousands place down to the ones place
        current_sum = 0

        if thousands_place > 0:
            # We only expect to see a 1 here, so we don't have to check for teens or anything like that
            current_sum += char_counts[thousands_place] + char_counts[1000]

        if hundreds_place > 0:
            current_sum += char_counts[hundreds_place] + char_counts[100]

        # Do we need an "and"?
        if (thousands_place + hundreds_place) > 0 and (ones_place + tens_place) > 0:
            current_sum += char_counts['and']

        # Is this thing a "teen"?
        is_teen = tens_place == 1

        # if it's a teen, do the teen lookup
        if is_teen:
            teen_to_look_up = i % 100
            current_sum += char_counts[teen_to_look_up]

        # tens place if it's not a teen
        if not is_teen and tens_place > 0:
            current_sum += char_counts[tens_place * 10]

        # ones place if it's not a teen:
        if not is_teen and ones_place > 0:
            current_sum += char_counts[ones_place]

        # Lastly, add it to the tally
        sum += current_sum

    return sum


@Problem(18)
def problem_18():
    """
    To solve this problem, we'll represent the pyramid as a 2d array, where the first dimension is the row and the
    second dimension is the elements in the row.

    The most scalable way to solve this problem is from the bottom-up.  Given some line, we can look at each element.
    For each element, we can look at it's children and take the greater of the two and add it to the parent.  If we
    repeat from bottom to top, the top-most element will contain the sum of the greatest path.

    For a pyramid (balanced binary tree) of N elements, this takes roughly N comparisons and N additions.
    :return:
    """

    pyramid = [
        [75],
        [95, 64],
        [17, 47, 82],
        [18, 35, 87, 10],
        [20, 4, 82, 47, 65],
        [19, 1, 23, 75, 3, 34],
        [88, 2, 77, 73, 7, 63, 67],
        [99, 65, 4, 28, 6, 16, 70, 92],
        [41, 41, 26, 56, 83, 40, 80, 70, 33],
        [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
        [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
        [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
        [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
        [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
        [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23],
    ]

    # We're going to iterate over every line of the pyramid, starting one up from the bottom and going to the top.  The
    # idea is that we want to look at the children directly under a given number, select the larger of the two, and add
    # it to the current number.  When we get to the top, pyramid[0][0] with have the greatest sum of all of the paths.

    # This range statement is confusing to read; len(pyramid) - 1 gives us the index of the final line; we want to start
    # one above that and go to 0-inclusive.
    for current_line_i in range(len(pyramid) - 1 - 1, 0 - 1, -1):
        current_line = pyramid[current_line_i]

        for current_value_i in range(0, len(current_line)):
            current_value = current_line[current_value_i]

            # Not-so-fancy index math
            child_line_i = current_line_i + 1
            left_child = pyramid[child_line_i][current_value_i]
            right_child = pyramid[child_line_i][current_value_i + 1]

            new_value = current_value + (left_child if left_child > right_child else right_child)
            current_line[current_value_i] = new_value

    return pyramid[0][0]


@Problem(19)
def problem_19():
    """
    This is a simple brute-force.  100 years * 365 days = a really small number of days to iterate through.  This
    problem is more of a classic highschool word problem than anything; they tell you that 1JAN1900 was a Monday and
    that they want you to calculate the number of Sundays on the first of the month starting in 1901.

    A few notes:

    1.  I purposely didn't use the date-time library; this can be solved easily enough without it.

    2.  Instead of iterating over every day, I could simply start at the first Sunday and iterate week by week.  If I
    were to do that, I would have to account for overflowing at the end of the month, etc.  I felt like it was simpler,
    albeit less efficient to write it this way.

    3.  If I were really, really fancy, I would maybe take a different approach and calculate what days are on the first
    of the month, as a list starting from 0 on 1JAN1901 and then try to calculate (perhaps through modular division?)
    which of those are Sundays.  This would require fewer additions (one per month, so 120 operations roughly) and 120
    divisions (to check every one of the first-of-month dates against a known offset).  This would be faster, but not
    noticeable at this scale.

    :return:
    """
    def days_in_month(month, year):
        std_dim = {
            1: 31,
            3: 31,
            4: 30,
            5: 31,
            6: 30,
            7: 31,
            8: 31,
            9: 30,
            10: 31,
            11: 30,
            12: 31
        }

        if month in std_dim:
            return std_dim[month]

        non_std_dim = {
            2: lambda year: 29 if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0) else 28
        }

        return non_std_dim[month](year)

    total_sundays_on_first = 0

    # dow go from 0 to 6 to represent Monday through Sunday, respectively.
    current_dow = 0

    for year in range(1900, 2000 + 1):
        for month in range(1, 12 + 1):
            dim = days_in_month(month, year)

            for day in range(1, dim + 1):
                if day == 1 and current_dow == 6 and year >= 1901:
                    total_sundays_on_first += 1

                # We're done our iteration; advance the day of week
                current_dow += 1
                if current_dow > 6:
                    current_dow = 0

    return total_sundays_on_first


@Problem(20)
def problem_20():
    """
    For this problem we're going to start off by asking for 100!.  We'll then loop the following steps until we're out
    of digits:

    1.  Get the last digit using mod-10
    2.  Add it to a running total
    3.  Truncate the last digit by doing an integer division by 10
    :return:
    """
    big_farking_number = math.factorial(100)
    digit_sum = 0

    while big_farking_number > 0:
        digit_sum += big_farking_number % 10
        big_farking_number = big_farking_number // 10

    return digit_sum


@Problem(21)
def problem_21():
    """
    In this one, we keep a map of N, d(N).  If we evaluate some number i, we can calculate d(i) and then consult the map
    to see if d(d(i)) == i.

    That's not confusing to read.

    Notes:

    1.  The get_sum_of_divisors is really inefficient.  I'll try every number between 1 and half the number being
    evaluated.  This is where the majority of the solution's time is spent.
    :return:
    """
    # Key:  number, value:  sum of number's proper divisors
    sum_of_divisor_map = dict()
    running_sum = 0

    def get_sum_of_divisors(n):
        sod = 0
        for i in range(1, (n // 2) + 1):
            if n % i == 0:
                sod += i
        return sod

    for i in range(2, 10000 + 1):
        sod = get_sum_of_divisors(i)
        if sod in sum_of_divisor_map:
            # Check to see if we have an amicable pair
            if i == sum_of_divisor_map[sod]:
                running_sum += i + sod
        else:
            sum_of_divisor_map[i] = sod

    return running_sum


@Problem(22)
def problem_22():
    """
    This solution is inefficient but runs in a reasonable amount of time.

    We read in the file, split it into a list, then build a new list that contains each name sans quotes in lower-case.

    We then sort the parsed list and iterate through each line.  For each line, we iterate through each letter to get
    it's value and, in turn, the word's value.  We then multiply the word value with the 1-based line number and keep a
    running total.

    BOOM.
    :return:
    """
    # Alright, first thing's first:  Let's read in that file.  It just so happens that PocketEuler already has it for us
    with open('../pocket-euler/files/names.txt', 'r') as content_file:
        content = content_file.read()

    # Let's go ahead and split the names into a list
    split_content = content.split(',')

    # Let's go through that list and strip the quotes and make them all lower-case
    names = list()
    for name in split_content:
        names.append(name.strip('"').lower())

    # sort them
    sorted_names = sorted(names)

    # For each name and line number, we'll calculate the name's value and keep a running total of the product.
    total = 0
    for i, name in enumerate(sorted_names):
        line_number = i + 1

        # Name value calculation
        name_total = 0
        for letter in name:
            letter_value = ord(letter) - ord('a') + 1
            name_total += letter_value

        total += name_total * line_number

    return total


@Problem(23)
def problem_23():
    """
    This solution is a bit memory inefficient, but it works.

    We find all of the abundant numbers by calculating the sum of the divisors between 1 and 28123, inclusive.  If the
    s.o.d. is greater than the number itself, it's abundant and we add it to a set.  We when make two copies of that set
    and loop through both of them in a nested loop.  This gives us every possible combination of every abundant number.
    We calculate each sum and add it to a set to eliminate dups.

    We then take this set of numbers-that-are-sums-of-abundant-numbers and diff that against a set that is every number
    from 1 to 28123, inclusive, to get our numbers-that-are-not-sums-of-abundant-numbers.

    We sum our final set and return it.

    This answer spends most of it's time finding divisors.
    :return:
    """
    def get_sum_of_divisors(n):
        sod = 0
        for i in range(1, (n // 2) + 1):
            if n % i == 0:
                sod += i
        return sod

    abundant_numbers = set()
    all_numbers = set(i for i in range(1, 28123 + 1))

    # Find all of the abundant numbers
    for i in all_numbers:
        if i < get_sum_of_divisors(i):
            abundant_numbers.add(i)

    numbers_from_abundant_numbers = set()

    # Find the sum of all combinations of all abundant numbers and store them in a set
    for i in set(abundant_numbers):
        for j in set(abundant_numbers):
            sum_of_abundant_numbers = i + j
            if sum_of_abundant_numbers <= 28123:
                numbers_from_abundant_numbers.add(sum_of_abundant_numbers)

    # Our answer is the difference between all_numbers and numbers_from_abundant_numbers
    numbers_that_are_not_sums_of_abundant_numbers = all_numbers.difference(numbers_from_abundant_numbers)
    return sum(numbers_that_are_not_sums_of_abundant_numbers)


@Problem(24)
def problem_24():
    """
    To solve this problem, we're going to count on itertools.permutations.  It just so happens that it iterates through
    the permutations "in order," so if we ask it to iterate one million times and we start with a list that's in lex
    order, it'll give us the one millionth item in lex order.
    :return:
    """
    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    # The trick here is to use itertools.permutations.  It just so happens that it will swap the elements in a
    # predictable order.  If we give it a sorted tuple, it'll iterate through in lexicographical order.

    p = itertools.permutations(digits)
    for i in range(1, 1000000 + 1):
        result = next(p)

    # At this point, we have a collection of digits.  We need to combine them into a single number
    final_number = 0
    for i in range(0, len(result)):
        # Grab this digit, multiply it buy the correct "place" and add it to the result
        final_number += result[i] * (10 ** (len(result) - i - 1))

    return final_number


@Problem(25)
def problem_25():
    """
    In this problem, we will use a loop to calculate a fib sequence.  We'll keep track of the number of iterations and
    test each output.  To test, we'll first calculate a number with 1000 digits and simply compare each iteration.
    :return:
    """
    target = 10 ** (1000 - 1)
    previous_f = [1, 1]
    i = 2
    result = 0
    while result < target:
        result = previous_f[0] + previous_f[1]
        i += 1
        previous_f[0] = previous_f[1]
        previous_f[1] = result
    return i
