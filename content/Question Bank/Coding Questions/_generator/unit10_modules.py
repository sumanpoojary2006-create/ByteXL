"""Unit 10 - Modules and Packages - Coding Questions (30: 10/10/10).

Scope: import / from-import / aliases and using the standard library. The coding
sandbox has no filesystem for custom modules, so every question exercises real
stdlib modules: math, statistics, collections, datetime, itertools, fractions,
decimal, heapq, calendar, random (seeded, deterministic), string, functools.
"""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from cqlib import main

TOPIC = "modules"
IMP, STD = "import", "standard-library"

Q = []

# ----------------------------- EASY (10) -----------------------------
Q.append(dict(
    title="Square Root", difficulty="Easy", topics=TOPIC, subTopics=STD,
    prose="Import the math module and use math.sqrt to print the square root of a "
          "number, rounded to 4 decimal places.",
    input_lines=["Line 1: A number"],
    inputs=["16", "2", "9", "0", "1", "100", "50"],
    solution="""
        import math
        n = int(input())
        print(round(math.sqrt(n), 4))
    """))

Q.append(dict(
    title="Factorial from Math", difficulty="Easy", topics=TOPIC, subTopics=STD,
    prose="Use math.factorial to print the factorial of a number read from input.",
    input_lines=["Line 1: A number"],
    inputs=["5", "0", "10", "1", "2", "7", "12"],
    solution="""
        import math
        print(math.factorial(int(input())))
    """))

Q.append(dict(
    title="GCD from Math", difficulty="Easy", topics=TOPIC, subTopics=IMP,
    prose="Use 'from math import gcd' to print the greatest common divisor of two "
          "numbers.",
    input_lines=["Line 1: First number", "Line 2: Second number"],
    inputs=["12\n18", "17\n5", "100\n25", "1\n1", "0\n5", "7\n7", "1000\n999"],
    solution="""
        from math import gcd
        a = int(input())
        b = int(input())
        print(gcd(a, b))
    """))

Q.append(dict(
    title="Floor and Ceiling", difficulty="Easy", topics=TOPIC, subTopics=STD,
    prose="Read a decimal number and use math.floor and math.ceil to print its "
          "floor and ceiling, separated by a space.",
    input_lines=["Line 1: A decimal number"],
    inputs=["3.4", "5.0", "-2.5", "0.0", "-0.5", "99.99", "-100.01"],
    solution="""
        import math
        x = float(input())
        print(math.floor(x), math.ceil(x))
    """))

Q.append(dict(
    title="Average with Statistics", difficulty="Easy", topics=TOPIC, subTopics=STD,
    prose="Use statistics.mean to print the average of a line of numbers, rounded "
          "to 2 decimal places.",
    input_lines=["Line 1: Space-separated numbers"],
    inputs=["1 2 3 4", "5", "10 20 30", "0", "-5 5", "1 2 3 4 5 6 7 8 9 10", "100 -100 50"],
    solution="""
        import statistics
        nums = list(map(int, input().split()))
        print(round(statistics.mean(nums), 2))
    """))

Q.append(dict(
    title="Median with Statistics", difficulty="Easy", topics=TOPIC, subTopics=STD,
    prose="Use statistics.median to print the median of a line of numbers.",
    input_lines=["Line 1: Space-separated numbers"],
    inputs=["1 2 3", "1 2 3 4", "5 5 5", "0", "-3 -1 -2", "1 2 3 4 5 6", "10 20"],
    solution="""
        import statistics
        nums = list(map(int, input().split()))
        print(statistics.median(nums))
    """))

Q.append(dict(
    title="Power from Math", difficulty="Easy", topics=TOPIC, subTopics=STD,
    prose="Use math.pow to print a raised to the power b as a whole number.",
    input_lines=["Line 1: base", "Line 2: exponent"],
    inputs=["2\n10", "3\n0", "5\n2", "0\n5", "1\n100", "10\n1", "-2\n3"],
    solution="""
        import math
        base = int(input())
        exp = int(input())
        print(round(math.pow(base, exp)))
    """))

Q.append(dict(
    title="Circle Area with Pi", difficulty="Easy", topics=TOPIC, subTopics=STD,
    prose="Use math.pi to print the area of a circle (pi * r * r) rounded to 2 "
          "decimal places.",
    input_lines=["Line 1: Radius"],
    inputs=["1", "2", "5", "0", "10", "3", "100"],
    solution="""
        import math
        r = int(input())
        print(round(math.pi * r * r, 2))
    """))

Q.append(dict(
    title="Hypotenuse", difficulty="Easy", topics=TOPIC, subTopics=STD,
    prose="Use math.hypot to print the length of the hypotenuse of a right triangle "
          "given its two shorter sides, rounded to 2 decimal places.",
    input_lines=["Line 1: First side", "Line 2: Second side"],
    inputs=["3\n4", "5\n12", "1\n1", "0\n5", "0\n0", "8\n15", "100\n100"],
    solution="""
        import math
        a = int(input())
        b = int(input())
        print(round(math.hypot(a, b), 2))
    """))

Q.append(dict(
    title="Base-10 Logarithm", difficulty="Easy", topics=TOPIC, subTopics=STD,
    prose="Use math.log10 to print the base-10 logarithm of a number, rounded to 4 "
          "decimal places.",
    input_lines=["Line 1: A positive number"],
    inputs=["100", "1000", "1", "10", "1000000", "5", "999"],
    solution="""
        import math
        n = int(input())
        print(round(math.log10(n), 4))
    """))

# ----------------------------- MEDIUM (10) -----------------------------
Q.append(dict(
    title="Most Common Word", difficulty="Medium", topics=TOPIC, subTopics=STD,
    prose="Use collections.Counter to find the most common word in a sentence. Print "
          "the word and its count separated by a space.",
    input_lines=["Line 1: A sentence"],
    inputs=["a b a c a", "x y", "p p q q q", "z", "m n m n m", "a a a a a a a a", "cat dog cat bird cat dog"],
    solution="""
        from collections import Counter
        words = input().split()
        word, count = Counter(words).most_common(1)[0]
        print(word, count)
    """))

Q.append(dict(
    title="Standard Deviation", difficulty="Medium", topics=TOPIC, subTopics=STD,
    prose="Use statistics.pstdev to print the population standard deviation of a "
          "line of numbers, rounded to 2 decimal places.",
    input_lines=["Line 1: Space-separated numbers"],
    inputs=["1 2 3 4 5", "10 10 10", "2 4 6", "0 0", "-5 5 -5 5", "1 2 3 4 5 6 7 8 9 10", "100 200"],
    solution="""
        import statistics
        nums = list(map(int, input().split()))
        print(round(statistics.pstdev(nums), 2))
    """))

Q.append(dict(
    title="GCD of a List", difficulty="Medium", topics=TOPIC, subTopics=IMP,
    prose="Use functools.reduce together with math.gcd to print the greatest common "
          "divisor of a whole line of numbers.",
    input_lines=["Line 1: Space-separated numbers"],
    inputs=["12 18 24", "7 14", "100 25 50", "5", "0 5", "1 1 1", "1000 500 250 100"],
    solution="""
        from functools import reduce
        from math import gcd
        nums = list(map(int, input().split()))
        print(reduce(gcd, nums))
    """))

Q.append(dict(
    title="Count Combinations", difficulty="Medium", topics=TOPIC, subTopics=STD,
    prose="Use math.comb to print how many ways there are to choose r items from n "
          "items.",
    input_lines=["Line 1: n", "Line 2: r"],
    inputs=["5\n2", "10\n0", "6\n3", "0\n0", "1\n1", "20\n10", "5\n5"],
    solution="""
        import math
        n = int(input())
        r = int(input())
        print(math.comb(n, r))
    """))

Q.append(dict(
    title="Count Permutations", difficulty="Medium", topics=TOPIC, subTopics=STD,
    prose="Use math.perm to print how many ordered arrangements there are of r items "
          "chosen from n items.",
    input_lines=["Line 1: n", "Line 2: r"],
    inputs=["5\n2", "4\n4", "6\n1", "0\n0", "1\n1", "10\n0", "5\n5"],
    solution="""
        import math
        n = int(input())
        r = int(input())
        print(math.perm(n, r))
    """))

Q.append(dict(
    title="Group by Parity", difficulty="Medium", topics=TOPIC, subTopics=STD,
    prose="Use collections.defaultdict to split a line of numbers into evens and "
          "odds. Print 'even:' followed by the even numbers, then 'odd:' followed "
          "by the odd numbers, keeping their original order.",
    input_lines=["Line 1: Space-separated numbers"],
    inputs=["1 2 3 4 5", "2 4", "1 3", "0", "-2 -1 0 1 2", "1 2 3 4 5 6 7 8 9 10", "7"],
    solution="""
        from collections import defaultdict
        groups = defaultdict(list)
        for x in map(int, input().split()):
            groups["even" if x % 2 == 0 else "odd"].append(x)
        print("even:", *groups["even"])
        print("odd:", *groups["odd"])
    """))

Q.append(dict(
    title="Day of the Week", difficulty="Medium", topics=TOPIC, subTopics=STD,
    prose="Use the datetime module to print the day of the week for a given date "
          "(for example 'Monday'). Read a date written as YYYY-MM-DD.",
    input_lines=["Line 1: A date as YYYY-MM-DD"],
    inputs=["2024-01-01", "2024-12-25", "2000-02-29", "1970-01-01", "1999-12-31",
            "2023-07-04", "2100-01-01"],
    solution="""
        from datetime import date
        parts = input().split("-")
        d = date(int(parts[0]), int(parts[1]), int(parts[2]))
        print(d.strftime("%A"))
    """))

Q.append(dict(
    title="Seeded Random", difficulty="Medium", topics=TOPIC, subTopics=STD,
    prose="Use the random module. Read a seed, seed the generator with it, and print "
          "a single random integer from 1 to 100. Seeding makes the result "
          "repeatable.",
    input_lines=["Line 1: The seed"],
    inputs=["1", "42", "100", "0", "7", "999", "12345"],
    solution="""
        import random
        seed = int(input())
        random.seed(seed)
        print(random.randint(1, 100))
    """))

Q.append(dict(
    title="Letters and Digits", difficulty="Medium", topics=TOPIC, subTopics=STD,
    prose="Use the string module's ascii_letters and digits to count how many "
          "letters and how many digits are in a line of text. Print the two counts "
          "separated by a space.",
    input_lines=["Line 1: A line of text"],
    inputs=["abc 123", "Hello World", "x9 y8", "12345", "abcde", "a1b2c3d4e5", "The Year Is 2024"],
    solution="""
        import string
        text = input()
        letters = sum(1 for c in text if c in string.ascii_letters)
        digits = sum(1 for c in text if c in string.digits)
        print(letters, digits)
    """))

Q.append(dict(
    title="Find the Mode", difficulty="Medium", topics=TOPIC, subTopics=STD,
    prose="Use statistics.mode to print the value that appears most often in a line "
          "of numbers.",
    input_lines=["Line 1: Space-separated numbers"],
    inputs=["1 2 2 3", "5 5 5", "1 1 2 2", "7", "-1 -1 -2", "1 2 3 3 3 4", "9 9 9 9 9 9"],
    solution="""
        import statistics
        nums = list(map(int, input().split()))
        print(statistics.mode(nums))
    """))

# ----------------------------- HARD (10) -----------------------------
Q.append(dict(
    title="Top K Words", difficulty="Hard", topics=TOPIC, subTopics=STD,
    prose="Use collections.Counter to print the K most common words in a sentence, "
          "one 'word count' per line, from most to least common.",
    input_lines=["Line 1: K", "Line 2: A sentence"],
    inputs=["2\na b a c b a", "1\nx x y", "3\np q r", "1\nz", "0\na b c",
            "5\na a b b c c d", "2\ncat cat dog dog dog bird"],
    solution="""
        from collections import Counter
        k = int(input())
        words = input().split()
        for word, count in Counter(words).most_common(k):
            print(word, count)
    """))

Q.append(dict(
    title="Pairs from Combinations", difficulty="Hard", topics=TOPIC, subTopics=STD,
    prose="Use itertools.combinations to count how many pairs of numbers add up to a "
          "target. Read a line of numbers and a target and print the count.",
    input_lines=["Line 1: Space-separated numbers", "Line 2: Target"],
    inputs=["1 2 3 4\n5", "1 1 1\n2", "5 6\n100", "5\n5", "0 0 0\n0",
            "1 2 3 4 5 6 7 8\n9", "-1 1 -2 2\n0"],
    solution="""
        from itertools import combinations
        nums = list(map(int, input().split()))
        target = int(input())
        print(sum(1 for a, b in combinations(nums, 2) if a + b == target))
    """))

Q.append(dict(
    title="Days Between Dates", difficulty="Hard", topics=TOPIC, subTopics=STD,
    prose="Use the datetime module to print how many days apart two dates are (a "
          "non-negative number). Read two dates written as YYYY-MM-DD.",
    input_lines=["Line 1: First date", "Line 2: Second date"],
    inputs=["2024-01-01\n2024-01-31", "2024-01-01\n2024-01-01", "2020-01-01\n2021-01-01",
            "2024-03-01\n2024-01-01", "1970-01-01\n1970-01-01", "2000-02-29\n2000-03-01",
            "1999-12-31\n2000-01-01"],
    solution="""
        from datetime import date
        def parse(s):
            y, m, d = s.split("-")
            return date(int(y), int(m), int(d))
        d1 = parse(input())
        d2 = parse(input())
        print(abs((d2 - d1).days))
    """))

Q.append(dict(
    title="Rotate with Deque", difficulty="Hard", topics=TOPIC, subTopics=STD,
    prose="Use collections.deque and its rotate method to rotate a list of numbers "
          "to the right by K places. Print the rotated list separated by spaces.",
    input_lines=["Line 1: Space-separated numbers", "Line 2: K"],
    inputs=["1 2 3 4 5\n2", "1 2 3\n0", "1 2\n3", "5\n0", "1 2 3 4 5\n5",
            "1 2 3 4 5\n-2", "1 2 3 4 5 6 7 8\n10"],
    solution="""
        from collections import deque
        nums = deque(map(int, input().split()))
        k = int(input())
        nums.rotate(k)
        print(*nums)
    """))

Q.append(dict(
    title="Common Words with Counts", difficulty="Hard", topics=TOPIC, subTopics=STD,
    prose="Use Counter intersection (the & operator) to find words appearing in both "
          "of two lines. For each shared word in sorted order, print 'word:count' "
          "where count is the smaller of the two counts.",
    input_lines=["Line 1: First sentence", "Line 2: Second sentence"],
    inputs=["a a b c\na b b", "x y\ny z", "p p\np p p", "a\nb", "x\nx",
            "a b c d\ne f g h", "cat cat dog\ndog dog cat"],
    solution="""
        from collections import Counter
        c1 = Counter(input().split())
        c2 = Counter(input().split())
        shared = c1 & c2
        for word in sorted(shared):
            print(f"{word}:{shared[word]}")
    """))

Q.append(dict(
    title="Leap Year Check", difficulty="Hard", topics=TOPIC, subTopics=STD,
    prose="Use calendar.isleap to print 'Yes' if a year is a leap year and 'No' "
          "otherwise.",
    input_lines=["Line 1: A year"],
    inputs=["2000", "1900", "2024", "1", "2100", "2023", "1600"],
    solution="""
        import calendar
        year = int(input())
        print("Yes" if calendar.isleap(year) else "No")
    """))

Q.append(dict(
    title="Sum of Fractions", difficulty="Hard", topics=TOPIC, subTopics=STD,
    prose="Use fractions.Fraction to add N fractions and print the exact result in "
          "lowest terms as 'p/q'. Read N, then N fractions written as 'a/b'.",
    input_lines=["Line 1: N", "Next N lines: a fraction 'a/b'"],
    inputs=["2\n1/2\n1/3", "1\n2/4", "3\n1/6\n1/6\n1/6", "1\n0/1", "0",
            "4\n1/2\n1/2\n1/2\n1/2", "2\n1/3\n2/3"],
    solution="""
        from fractions import Fraction
        n = int(input())
        total = Fraction(0)
        for _ in range(n):
            total += Fraction(input())
        print(f"{total.numerator}/{total.denominator}")
    """))

Q.append(dict(
    title="Exact Decimal Sum", difficulty="Hard", topics=TOPIC, subTopics=STD,
    prose="Use decimal.Decimal to add two decimal numbers without floating-point "
          "rounding error, and print the exact sum. Read the two numbers as text.",
    input_lines=["Line 1: First decimal", "Line 2: Second decimal"],
    inputs=["0.1\n0.2", "1.5\n2.5", "0.01\n0.02", "0\n0", "-1.5\n1.5",
            "100.001\n0.999", "-0.1\n-0.2"],
    solution="""
        from decimal import Decimal
        a = Decimal(input())
        b = Decimal(input())
        print(a + b)
    """))

Q.append(dict(
    title="K Largest with Heapq", difficulty="Hard", topics=TOPIC, subTopics=STD,
    prose="Use heapq.nlargest to print the K largest numbers from a list, in "
          "descending order, separated by spaces.",
    input_lines=["Line 1: K", "Line 2: Space-separated numbers"],
    inputs=["2\n3 1 4 1 5", "1\n7 2", "3\n5 5 5", "0\n1 2 3", "1\n0",
            "5\n1 2 3 4 5 6 7 8 9 10", "2\n-5 -1 -10"],
    solution="""
        import heapq
        k = int(input())
        nums = list(map(int, input().split()))
        print(*heapq.nlargest(k, nums))
    """))

Q.append(dict(
    title="Prime Factors", difficulty="Hard", topics=TOPIC, subTopics=STD,
    prose="Use math.isqrt to help print the prime factors of a number in increasing "
          "order, separated by spaces (a factor is listed once for each time it "
          "divides the number).",
    input_lines=["Line 1: A whole number greater than 1"],
    inputs=["12", "17", "60", "2", "97", "1024", "999"],
    solution="""
        import math
        n = int(input())
        factors = []
        d = 2
        while d <= math.isqrt(n):
            while n % d == 0:
                factors.append(d)
                n //= d
            d += 1
        if n > 1:
            factors.append(n)
        print(*factors)
    """))

if __name__ == "__main__":
    out = os.path.abspath(os.path.join(
        os.path.dirname(__file__), "..",
        "Unit 10 - Modules and Packages",
        "Unit 10 - Modules and Packages - Coding Questions.xlsx"))
    os.makedirs(os.path.dirname(out), exist_ok=True)
    main(Q, out)
