"""Unit 4 - Looping - Coding Questions (30: 10 Easy / 10 Medium / 10 Hard).

Scope: while loops, for loops, range(), iterating sequences/strings,
break/continue, nested loops and patterns. No functions/OOP/collections methods
beyond what Units 1-3 + basic loops cover.
"""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from cqlib import main

TOPIC = "loops-and-iteration"
FOR, WHILE, NEST = "for-loops-and-range", "while-loops", "nested-loops"

Q = []

# ----------------------------- EASY (10) -----------------------------
Q.append(dict(
    title="Daily Steps Total", difficulty="Easy", topics=TOPIC, subTopics=FOR,
    prose="A fitness app adds up a running total from day 1 to day N. Read N and "
          "print the sum of all whole numbers from 1 to N.",
    input_lines=["Line 1: N, the number of days"],
    inputs=["5", "10", "1", "2", "20", "50", "7"],
    solution="""
        n = int(input())
        total = 0
        for i in range(1, n + 1):
            total += i
        print(total)
    """))

Q.append(dict(
    title="Rocket Countdown", difficulty="Easy", topics=TOPIC, subTopics=FOR,
    prose="A launch console counts down before lift-off. Read N and print every "
          "number from N down to 1, one per line.",
    input_lines=["Line 1: N, the starting number"],
    inputs=["5", "3", "1", "2", "10", "7", "4"],
    solution="""
        n = int(input())
        for i in range(n, 0, -1):
            print(i)
    """))

Q.append(dict(
    title="Times Table", difficulty="Easy", topics=TOPIC, subTopics=FOR,
    prose="A maths tutor app prints the multiplication table of a number. Read N "
          "and print its table from 1 to 10 in the form 'N x i = value'.",
    input_lines=["Line 1: N, the number"],
    inputs=["2", "5", "9", "1", "0", "12", "7"],
    solution="""
        n = int(input())
        for i in range(1, 11):
            print(n, "x", i, "=", n * i)
    """))

Q.append(dict(
    title="Vowel Counter", difficulty="Easy", topics=TOPIC, subTopics=FOR,
    prose="A spelling game counts the vowels in a word. Read one line of text and "
          "print how many vowels (a, e, i, o, u) it contains, ignoring case.",
    input_lines=["Line 1: A line of text"],
    inputs=["education", "Rhythm", "AEIOU", "a", "xyz", "Programming", "Umbrella"],
    solution="""
        text = input()
        count = 0
        for ch in text.lower():
            if ch in "aeiou":
                count += 1
        print(count)
    """))

Q.append(dict(
    title="Cash Register Total", difficulty="Easy", topics=TOPIC, subTopics=FOR,
    prose="A shop till adds up the prices of N items. Read N, then read N prices on "
          "separate lines and print their total.",
    input_lines=["Line 1: N, the number of items", "Next N lines: one price each"],
    inputs=["3\n10\n20\n30", "1\n5", "4\n1\n2\n3\n4", "2\n0\n0", "5\n100\n200\n300\n400\n500",
            "1\n999", "6\n1\n1\n1\n1\n1\n1"],
    solution="""
        n = int(input())
        total = 0
        for _ in range(n):
            total += int(input())
        print(total)
    """))

Q.append(dict(
    title="Factorial Machine", difficulty="Easy", topics=TOPIC, subTopics=FOR,
    prose="A calculator computes the factorial of N (the product 1 x 2 x ... x N; "
          "0! is 1). Read N and print N!.",
    input_lines=["Line 1: N"],
    inputs=["5", "0", "6", "1", "3", "7", "10"],
    solution="""
        n = int(input())
        fact = 1
        for i in range(1, n + 1):
            fact *= i
        print(fact)
    """))

Q.append(dict(
    title="Even Numbers List", difficulty="Easy", topics=TOPIC, subTopics=FOR,
    prose="A number-line poster shows all even numbers up to a limit. Read N and "
          "print every even number from 2 up to N, one per line.",
    input_lines=["Line 1: N, the upper limit"],
    inputs=["10", "8", "2", "1", "0", "20", "15"],
    solution="""
        n = int(input())
        for i in range(2, n + 1, 2):
            print(i)
    """))

Q.append(dict(
    title="Class Average", difficulty="Easy", topics=TOPIC, subTopics=FOR,
    prose="A teacher averages N test scores. Read N, then read N scores on separate "
          "lines and print their average rounded to 2 decimal places.",
    input_lines=["Line 1: N", "Next N lines: one score each"],
    inputs=["3\n80\n90\n70", "2\n50\n75", "1\n42", "1\n0", "4\n60\n70\n80\n90",
            "5\n100\n100\n100\n100\n100", "2\n33\n67"],
    solution="""
        n = int(input())
        total = 0
        for _ in range(n):
            total += int(input())
        print(round(total / n, 2))
    """))

Q.append(dict(
    title="String Reverser", difficulty="Easy", topics=TOPIC, subTopics=FOR,
    prose="A word-game shows a word spelled backwards. Read one line and print its "
          "characters in reverse order, building the result with a loop.",
    input_lines=["Line 1: A line of text"],
    inputs=["hello", "level", "Python", "a", "racecar", "OpenAI", "Coding"],
    solution="""
        text = input()
        result = ""
        for ch in text:
            result = ch + result
        print(result)
    """))

Q.append(dict(
    title="Digit Counter", difficulty="Easy", topics=TOPIC, subTopics=WHILE,
    prose="A form validator counts how many digits a number has. Read a whole "
          "number and print the number of digits it contains.",
    input_lines=["Line 1: A whole number"],
    inputs=["12345", "7", "100000", "0", "-45", "999999999", "10"],
    solution="""
        n = int(input())
        n = abs(n)
        count = 0
        while n > 0:
            count += 1
            n //= 10
        if count == 0:
            count = 1
        print(count)
    """))

# ----------------------------- MEDIUM (10) -----------------------------
Q.append(dict(
    title="Sum of Even Numbers", difficulty="Medium", topics=TOPIC, subTopics=FOR,
    prose="An energy meter sums only the even readings from 1 to N. Read N and "
          "print the total of all even numbers in that range.",
    input_lines=["Line 1: N"],
    inputs=["10", "5", "1", "0", "2", "20", "9"],
    solution="""
        n = int(input())
        total = 0
        for i in range(1, n + 1):
            if i % 2 == 0:
                total += i
        print(total)
    """))

Q.append(dict(
    title="Above the Bar", difficulty="Medium", topics=TOPIC, subTopics=FOR,
    prose="A results board counts how many scores beat a cut-off. Read N, then a "
          "line of N scores, then the cut-off, and print how many scores are "
          "strictly greater than the cut-off.",
    input_lines=["Line 1: N", "Line 2: N space-separated scores", "Line 3: The cut-off"],
    inputs=["5\n10 20 30 40 50\n25", "3\n1 2 3\n5", "4\n7 8 9 10\n8",
            "1\n5\n0", "6\n-1 -2 3 4 5 6\n2", "3\n100 200 300\n1000",
            "2\n5 5\n5"],
    solution="""
        n = int(input())
        nums = list(map(int, input().split()))
        cutoff = int(input())
        count = 0
        for x in nums:
            if x > cutoff:
                count += 1
        print(count)
    """))

Q.append(dict(
    title="Highest Reading", difficulty="Medium", topics=TOPIC, subTopics=FOR,
    prose="A weather log finds the highest temperature of the day. Read N, then a "
          "line of N temperatures, and print the largest one using a loop.",
    input_lines=["Line 1: N", "Line 2: N space-separated numbers"],
    inputs=["5\n3 9 2 7 5", "3\n-1 -5 -3", "1\n42",
            "2\n0 0", "4\n10 20 30 40", "6\n-5 -1 -9 -3 -2 -8", "3\n100 5 3"],
    solution="""
        n = int(input())
        nums = list(map(int, input().split()))
        largest = nums[0]
        for x in nums[1:]:
            if x > largest:
                largest = x
        print(largest)
    """))

Q.append(dict(
    title="FizzBuzz", difficulty="Medium", topics=TOPIC, subTopics=FOR,
    prose="Print the numbers 1 to N, but replace multiples of 3 with 'Fizz', "
          "multiples of 5 with 'Buzz', and multiples of both with 'FizzBuzz'. "
          "Print one value per line.",
    input_lines=["Line 1: N"],
    inputs=["5", "15", "3", "1", "30", "45", "20"],
    solution="""
        n = int(input())
        for i in range(1, n + 1):
            if i % 15 == 0:
                print("FizzBuzz")
            elif i % 3 == 0:
                print("Fizz")
            elif i % 5 == 0:
                print("Buzz")
            else:
                print(i)
    """))

Q.append(dict(
    title="Digit Sum", difficulty="Medium", topics=TOPIC, subTopics=WHILE,
    prose="A checksum tool adds up the digits of a number. Read a whole number and "
          "print the sum of its digits.",
    input_lines=["Line 1: A whole number"],
    inputs=["1234", "9", "1000", "0", "-567", "999999", "42"],
    solution="""
        n = abs(int(input()))
        total = 0
        while n > 0:
            total += n % 10
            n //= 10
        print(total)
    """))

Q.append(dict(
    title="Character Frequency", difficulty="Medium", topics=TOPIC, subTopics=FOR,
    prose="A text tool counts how many times a specific character appears. Read a "
          "line of text, then a single character, and print how many times that "
          "character occurs in the text.",
    input_lines=["Line 1: A line of text", "Line 2: A single character"],
    inputs=["banana\na", "mississippi\ns", "hello\nz",
            "a\na", "aaaaaa\na", "programming\ng", "Testing\nT"],
    solution="""
        text = input()
        target = input()
        count = 0
        for ch in text:
            if ch == target:
                count += 1
        print(count)
    """))

Q.append(dict(
    title="Fibonacci Terms", difficulty="Medium", topics=TOPIC, subTopics=FOR,
    prose="Print the first N terms of the Fibonacci sequence (starting 0, 1) on a "
          "single line, separated by spaces.",
    input_lines=["Line 1: N, the number of terms"],
    inputs=["5", "1", "8", "0", "2", "12", "10"],
    solution="""
        n = int(input())
        a, b = 0, 1
        result = []
        for _ in range(n):
            result.append(a)
            a, b = b, a + b
        print(*result)
    """))

Q.append(dict(
    title="Greatest Common Divisor", difficulty="Medium", topics=TOPIC, subTopics=WHILE,
    prose="Read two whole numbers and print their greatest common divisor using "
          "repeated remainders (Euclid's method).",
    input_lines=["Line 1: First number", "Line 2: Second number"],
    inputs=["12\n18", "17\n5", "100\n25", "1\n1", "0\n5", "48\n18", "7\n7"],
    solution="""
        a = int(input())
        b = int(input())
        while b != 0:
            a, b = b, a % b
        print(a)
    """))

Q.append(dict(
    title="Prime Check", difficulty="Medium", topics=TOPIC, subTopics=FOR,
    prose="Read a whole number and print 'Prime' if it is a prime number, otherwise "
          "print 'Not Prime'.",
    input_lines=["Line 1: A whole number"],
    inputs=["7", "10", "1", "0", "2", "97", "-5"],
    solution="""
        n = int(input())
        if n < 2:
            print("Not Prime")
        else:
            is_prime = True
            for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0:
                    is_prime = False
                    break
            print("Prime" if is_prime else "Not Prime")
    """))

Q.append(dict(
    title="Reverse a Number", difficulty="Medium", topics=TOPIC, subTopics=WHILE,
    prose="Read a whole number and print it with its digits reversed (drop any "
          "leading zeros that result).",
    input_lines=["Line 1: A whole number"],
    inputs=["1234", "100", "5", "0", "-89", "987654", "20"],
    solution="""
        n = int(input())
        sign = -1 if n < 0 else 1
        n = abs(n)
        rev = 0
        while n > 0:
            rev = rev * 10 + n % 10
            n //= 10
        print(sign * rev)
    """))

# ----------------------------- HARD (10) -----------------------------
Q.append(dict(
    title="Star Staircase", difficulty="Hard", topics=TOPIC, subTopics=NEST,
    prose="Print a left-aligned right triangle of stars with N rows: row i has i "
          "stars.",
    input_lines=["Line 1: N, the number of rows"],
    inputs=["4", "1", "5", "2", "0", "8", "6"],
    solution="""
        n = int(input())
        for i in range(1, n + 1):
            print("*" * i)
    """))

Q.append(dict(
    title="Multiplication Grid", difficulty="Hard", topics=TOPIC, subTopics=NEST,
    prose="Print an N by N grid where the cell in row i, column j holds i x j. "
          "Separate values in a row with single spaces.",
    input_lines=["Line 1: N"],
    inputs=["3", "2", "4", "1", "0", "6", "5"],
    solution="""
        n = int(input())
        for i in range(1, n + 1):
            row = []
            for j in range(1, n + 1):
                row.append(i * j)
            print(*row)
    """))

Q.append(dict(
    title="Floyd's Triangle", difficulty="Hard", topics=TOPIC, subTopics=NEST,
    prose="Print Floyd's triangle with N rows: fill consecutive counting numbers "
          "starting at 1, where row i contains i numbers.",
    input_lines=["Line 1: N"],
    inputs=["3", "1", "4", "2", "0", "6", "5"],
    solution="""
        n = int(input())
        num = 1
        for i in range(1, n + 1):
            row = []
            for _ in range(i):
                row.append(num)
                num += 1
            print(*row)
    """))

Q.append(dict(
    title="Count the Primes", difficulty="Hard", topics=TOPIC, subTopics=NEST,
    prose="Read N and print how many prime numbers there are from 2 up to and "
          "including N.",
    input_lines=["Line 1: N"],
    inputs=["10", "20", "2", "0", "1", "50", "30"],
    solution="""
        n = int(input())
        count = 0
        for num in range(2, n + 1):
            is_prime = True
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                count += 1
        print(count)
    """))

Q.append(dict(
    title="Pairs That Add Up", difficulty="Hard", topics=TOPIC, subTopics=NEST,
    prose="Read N, a line of N numbers, and a target. Count how many pairs of "
          "positions (i before j) have values that add up to the target.",
    input_lines=["Line 1: N", "Line 2: N space-separated numbers", "Line 3: Target"],
    inputs=["4\n1 2 3 4\n5", "3\n1 1 1\n2", "3\n5 6 7\n100",
            "1\n5\n5", "2\n0 0\n0", "6\n1 2 3 4 5 6\n7", "5\n-1 -2 3 4 5\n2"],
    solution="""
        n = int(input())
        nums = list(map(int, input().split()))
        target = int(input())
        count = 0
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    count += 1
        print(count)
    """))

Q.append(dict(
    title="Row Totals", difficulty="Hard", topics=TOPIC, subTopics=NEST,
    prose="Read a grid with R rows and C columns, then print the sum of each row on "
          "its own line, top to bottom.",
    input_lines=["Line 1: R and C separated by a space",
                 "Next R lines: C space-separated numbers each"],
    inputs=["2 3\n1 2 3\n4 5 6", "1 1\n99", "3 2\n1 1\n2 2\n3 3",
            "1 1\n0", "2 2\n-1 -2\n-3 -4", "4 1\n5\n10\n15\n20",
            "3 3\n1 2 3\n4 5 6\n7 8 9"],
    solution="""
        r, c = map(int, input().split())
        for _ in range(r):
            nums = list(map(int, input().split()))
            print(sum(nums))
    """))

Q.append(dict(
    title="Inverted Star Triangle", difficulty="Hard", topics=TOPIC, subTopics=NEST,
    prose="Print an inverted triangle of stars with N rows: the first row has N "
          "stars and each row below has one fewer, down to a single star.",
    input_lines=["Line 1: N"],
    inputs=["4", "1", "3", "2", "0", "7", "6"],
    solution="""
        n = int(input())
        for i in range(n, 0, -1):
            print("*" * i)
    """))

Q.append(dict(
    title="Student Averages", difficulty="Hard", topics=TOPIC, subTopics=NEST,
    prose="Read N and M, then N lines each holding M marks. For each student print "
          "their average mark rounded to 2 decimal places, one per line.",
    input_lines=["Line 1: N (students) and M (subjects), space-separated",
                 "Next N lines: M space-separated marks each"],
    inputs=["2 3\n80 90 100\n60 70 80", "1 2\n50 75", "2 2\n100 100\n0 0",
            "1 1\n0", "3 2\n10 20\n30 40\n50 60", "1 4\n90 80 70 60",
            "4 3\n1 2 3\n4 5 6\n7 8 9\n10 11 12"],
    solution="""
        n, m = map(int, input().split())
        for _ in range(n):
            marks = list(map(int, input().split()))
            print(round(sum(marks) / m, 2))
    """))

Q.append(dict(
    title="Repeated Digit Triangle", difficulty="Hard", topics=TOPIC, subTopics=NEST,
    prose="Print a triangle with N rows where row i shows the digit i repeated i "
          "times (for example row 3 is '333'). N is at most 9.",
    input_lines=["Line 1: N (1 to 9)"],
    inputs=["3", "1", "5", "2", "9", "7", "4"],
    solution="""
        n = int(input())
        for i in range(1, n + 1):
            print(str(i) * i)
    """))

Q.append(dict(
    title="Biggest in the Grid", difficulty="Hard", topics=TOPIC, subTopics=NEST,
    prose="Read a grid with R rows and C columns and print the single largest value "
          "found anywhere in the grid.",
    input_lines=["Line 1: R and C separated by a space",
                 "Next R lines: C space-separated numbers each"],
    inputs=["2 3\n1 5 3\n9 2 4", "1 1\n7", "2 2\n-1 -2\n-3 -4",
            "1 1\n0", "3 3\n1 2 3\n4 5 6\n7 8 9", "1 4\n10 20 30 40",
            "4 1\n-5\n-10\n-1\n-20"],
    solution="""
        r, c = map(int, input().split())
        best = None
        for _ in range(r):
            nums = list(map(int, input().split()))
            for x in nums:
                if best is None or x > best:
                    best = x
        print(best)
    """))

if __name__ == "__main__":
    out = os.path.abspath(os.path.join(
        os.path.dirname(__file__), "..",
        "Unit 4 - Looping",
        "Unit 4 - Looping - Coding Questions.xlsx"))
    os.makedirs(os.path.dirname(out), exist_ok=True)
    main(Q, out)
