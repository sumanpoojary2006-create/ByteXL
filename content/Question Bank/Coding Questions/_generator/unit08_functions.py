"""Unit 8 - Functions - Coding Questions (30: 10/10/10).

Scope: defining/calling, parameters & return, default/keyword args, *args,
lambda, map/filter/reduce, useful builtins, nested functions/closures,
scope, recursion.
"""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from cqlib import main

TOPIC = "functions"
DEF, PARAM, REC = "defining-and-calling-functions", "function-parameters-and-arguments", "recursion"

Q = []

# ----------------------------- EASY (10) -----------------------------
Q.append(dict(
    title="Square Function", difficulty="Easy", topics=TOPIC, subTopics=DEF,
    prose="Write a function that returns the square of a number, then use it to "
          "print the square of the number that is read from input.",
    input_lines=["Line 1: A number"],
    inputs=["5", "0", "-3", "1", "10", "-1", "100"],
    solution="""
        def square(x):
            return x * x

        n = int(input())
        print(square(n))
    """))

Q.append(dict(
    title="Greeting Function", difficulty="Easy", topics=TOPIC, subTopics=DEF,
    prose="Write a function that takes a name and returns the greeting 'Hello, "
          "<name>!'. Read a name and print the greeting.",
    input_lines=["Line 1: A name"],
    inputs=["Asha", "Kabir", "Sam", "A", "Priya", "Z", "Mohammed"],
    solution="""
        def greet(name):
            return f"Hello, {name}!"

        print(greet(input()))
    """))

Q.append(dict(
    title="Add Two Numbers", difficulty="Easy", topics=TOPIC, subTopics=PARAM,
    prose="Write a function that returns the sum of two numbers. Read two numbers "
          "and print their sum using the function.",
    input_lines=["Line 1: First number", "Line 2: Second number"],
    inputs=["3\n4", "10\n-5", "0\n0", "1\n1", "-10\n-20", "1000\n2000", "-7\n7"],
    solution="""
        def add(a, b):
            return a + b

        x = int(input())
        y = int(input())
        print(add(x, y))
    """))

Q.append(dict(
    title="Max of Two", difficulty="Easy", topics=TOPIC, subTopics=PARAM,
    prose="Write a function that returns the larger of two numbers. Read two numbers "
          "and print the larger one.",
    input_lines=["Line 1: First number", "Line 2: Second number"],
    inputs=["3\n9", "-1\n-5", "4\n4", "0\n0", "-5\n5", "100\n99", "-1000\n1000"],
    solution="""
        def bigger(a, b):
            return a if a >= b else b

        x = int(input())
        y = int(input())
        print(bigger(x, y))
    """))

Q.append(dict(
    title="Even or Odd", difficulty="Easy", topics=TOPIC, subTopics=DEF,
    prose="Write a function that returns 'Even' if a number is even and 'Odd' "
          "otherwise. Read a number and print the result.",
    input_lines=["Line 1: A number"],
    inputs=["4", "7", "0", "1", "-2", "-3", "1000000"],
    solution="""
        def even_or_odd(n):
            return "Even" if n % 2 == 0 else "Odd"

        print(even_or_odd(int(input())))
    """))

Q.append(dict(
    title="Rectangle Area", difficulty="Easy", topics=TOPIC, subTopics=PARAM,
    prose="Write a function that returns the area of a rectangle given its width and "
          "height. Read the width and height and print the area.",
    input_lines=["Line 1: Width", "Line 2: Height"],
    inputs=["3\n4", "5\n5", "2\n10", "1\n1", "0\n5", "7\n3", "100\n100"],
    solution="""
        def area(width, height):
            return width * height

        w = int(input())
        h = int(input())
        print(area(w, h))
    """))

Q.append(dict(
    title="To Fahrenheit", difficulty="Easy", topics=TOPIC, subTopics=PARAM,
    prose="Write a function that converts a Celsius temperature to Fahrenheit using "
          "F = C * 9 / 5 + 32. Read a Celsius value and print the Fahrenheit value "
          "rounded to 1 decimal place.",
    input_lines=["Line 1: Temperature in Celsius"],
    inputs=["0", "100", "37", "-40", "-273.15", "98.6", "1000"],
    solution="""
        def to_fahrenheit(c):
            return c * 9 / 5 + 32

        print(round(to_fahrenheit(float(input())), 1))
    """))

Q.append(dict(
    title="My Absolute", difficulty="Easy", topics=TOPIC, subTopics=DEF,
    prose="Write your own function that returns the absolute value of a number "
          "(without using the built-in abs). Read a number and print its absolute "
          "value.",
    input_lines=["Line 1: A number"],
    inputs=["-5", "5", "0", "1", "-1", "-1000000", "1000000"],
    solution="""
        def absolute(n):
            return -n if n < 0 else n

        print(absolute(int(input())))
    """))

Q.append(dict(
    title="Cube It", difficulty="Easy", topics=TOPIC, subTopics=DEF,
    prose="Write a function that returns the cube of a number. Read a number and "
          "print its cube.",
    input_lines=["Line 1: A number"],
    inputs=["2", "3", "-1", "0", "1", "-5", "10"],
    solution="""
        def cube(x):
            return x * x * x

        print(cube(int(input())))
    """))

Q.append(dict(
    title="Word Length", difficulty="Easy", topics=TOPIC, subTopics=PARAM,
    prose="Write a function that returns the number of characters in a word. Read a "
          "word and print its length using the function.",
    input_lines=["Line 1: A word"],
    inputs=["hello", "a", "coding", "x", "abcdefghij", "supercalifragilistic", "z"],
    solution="""
        def length(word):
            return len(word)

        print(length(input()))
    """))

# ----------------------------- MEDIUM (10) -----------------------------
Q.append(dict(
    title="Greet With Title", difficulty="Medium", topics=TOPIC, subTopics=PARAM,
    prose="Write a function greet(name, title='Friend') that returns 'Hello <title> "
          "<name>'. Read a name and a title; if the title line is empty, rely on "
          "the default. Print the greeting.",
    input_lines=["Line 1: A name", "Line 2: A title (may be empty or absent)"],
    inputs=["Asha\nDr", "Kabir", "Sam\nProf", "Lee\nMr", "Zoe", "Ann\nMs", "Ray\nCapt"],
    solution="""
        def greet(name, title="Friend"):
            return f"Hello {title} {name}"

        name = input()
        try:
            title = input()
        except EOFError:
            title = ""
        print(greet(name, title) if title else greet(name))
    """))

Q.append(dict(
    title="Sum All Arguments", difficulty="Medium", topics=TOPIC, subTopics=PARAM,
    prose="Write a function that accepts any number of arguments using *args and "
          "returns their sum. Read a line of numbers and print their total by "
          "unpacking them into the function.",
    input_lines=["Line 1: Space-separated numbers"],
    inputs=["1 2 3 4", "5", "10 -5", "0", "-1 -2 -3", "1 2 3 4 5 6 7 8", "100 200 300"],
    solution="""
        def total(*args):
            return sum(args)

        nums = list(map(int, input().split()))
        print(total(*nums))
    """))

Q.append(dict(
    title="Factorial Function", difficulty="Medium", topics=TOPIC, subTopics=DEF,
    prose="Write a function that returns the factorial of a number. Read a number "
          "and print its factorial.",
    input_lines=["Line 1: A number"],
    inputs=["5", "0", "6", "1", "10", "2", "3"],
    solution="""
        def factorial(n):
            result = 1
            for i in range(2, n + 1):
                result *= i
            return result

        print(factorial(int(input())))
    """))

Q.append(dict(
    title="Digit Sum Function", difficulty="Medium", topics=TOPIC, subTopics=DEF,
    prose="Write a function that returns the sum of the digits of a whole number. "
          "Read a number and print the digit sum.",
    input_lines=["Line 1: A whole number"],
    inputs=["1234", "9", "1000", "0", "-45", "999999", "10"],
    solution="""
        def digit_sum(n):
            n = abs(n)
            total = 0
            while n > 0:
                total += n % 10
                n //= 10
            return total

        print(digit_sum(int(input())))
    """))

Q.append(dict(
    title="Map to Squares", difficulty="Medium", topics=TOPIC, subTopics=DEF,
    prose="Read a line of numbers and use map with a lambda to print each number "
          "squared, in order, separated by spaces.",
    input_lines=["Line 1: Space-separated numbers"],
    inputs=["1 2 3", "4", "-2 5", "0", "-1 -2 -3", "1 2 3 4 5 6 7", "10 -10"],
    solution="""
        nums = list(map(int, input().split()))
        print(*map(lambda x: x * x, nums))
    """))

Q.append(dict(
    title="Filter Evens", difficulty="Medium", topics=TOPIC, subTopics=DEF,
    prose="Read a line of numbers and use filter with a lambda to print only the "
          "even numbers, in order, separated by spaces.",
    input_lines=["Line 1: Space-separated numbers"],
    inputs=["1 2 3 4 5 6", "10 15 20", "2 4 6", "1 3 5", "0", "-2 -4 3", "1 2 3 4 5 6 7 8 9 10"],
    solution="""
        nums = list(map(int, input().split()))
        print(*filter(lambda x: x % 2 == 0, nums))
    """))

Q.append(dict(
    title="Sort by Absolute Value", difficulty="Medium", topics=TOPIC, subTopics=DEF,
    prose="Read a line of numbers and print them sorted by their absolute value "
          "from smallest to largest, using a lambda as the sort key.",
    input_lines=["Line 1: Space-separated numbers"],
    inputs=["-3 1 -2", "5 -5 2", "-1 -2 -3", "0", "0 -1 1", "10 -3 -10 3", "1 2 3 4 5"],
    solution="""
        nums = list(map(int, input().split()))
        print(*sorted(nums, key=lambda x: abs(x)))
    """))

Q.append(dict(
    title="Count Vowels Function", difficulty="Medium", topics=TOPIC, subTopics=DEF,
    prose="Write a function that returns how many vowels are in a piece of text "
          "(ignoring case). Read a line and print the vowel count.",
    input_lines=["Line 1: A line of text"],
    inputs=["education", "xyz", "AEIOU", "a", "bcdfg", "The Quick Brown Fox", "aaaaaaaaaa"],
    solution="""
        def count_vowels(text):
            count = 0
            for ch in text.lower():
                if ch in "aeiou":
                    count += 1
            return count

        print(count_vowels(input()))
    """))

Q.append(dict(
    title="Min and Max", difficulty="Medium", topics=TOPIC, subTopics=PARAM,
    prose="Write a function that returns both the smallest and largest of a list of "
          "numbers. Read a line of numbers and print the smallest and largest "
          "separated by a space.",
    input_lines=["Line 1: Space-separated numbers"],
    inputs=["3 1 4 1 5", "7", "-1 -2", "0", "-5 -3 -8", "1 2 3 4 5 6 7 8 9", "100 -100"],
    solution="""
        def extremes(nums):
            return min(nums), max(nums)

        nums = list(map(int, input().split()))
        low, high = extremes(nums)
        print(low, high)
    """))

Q.append(dict(
    title="Product with Reduce", difficulty="Medium", topics=TOPIC, subTopics=DEF,
    prose="Read a line of numbers and use functools.reduce with a lambda to print "
          "the product of all of them.",
    input_lines=["Line 1: Space-separated numbers"],
    inputs=["1 2 3 4", "5", "2 2 2", "0 5 6", "1", "-1 2 -3", "1 2 3 4 5"],
    solution="""
        from functools import reduce

        nums = list(map(int, input().split()))
        print(reduce(lambda a, b: a * b, nums))
    """))

# ----------------------------- HARD (10) -----------------------------
Q.append(dict(
    title="Recursive Factorial", difficulty="Hard", topics=TOPIC, subTopics=REC,
    prose="Write a recursive function that returns the factorial of a number "
          "(no loops). Read a number and print its factorial.",
    input_lines=["Line 1: A number"],
    inputs=["5", "0", "7", "1", "10", "2", "3"],
    solution="""
        def factorial(n):
            if n <= 1:
                return 1
            return n * factorial(n - 1)

        print(factorial(int(input())))
    """))

Q.append(dict(
    title="Recursive Fibonacci", difficulty="Hard", topics=TOPIC, subTopics=REC,
    prose="Write a recursive function that returns the Nth Fibonacci number, where "
          "position 0 is 0 and position 1 is 1. Read N and print that Fibonacci "
          "number.",
    input_lines=["Line 1: N, the position"],
    inputs=["7", "0", "10", "1", "2", "15", "20"],
    solution="""
        def fib(n):
            if n < 2:
                return n
            return fib(n - 1) + fib(n - 2)

        print(fib(int(input())))
    """))

Q.append(dict(
    title="Recursive Digit Sum", difficulty="Hard", topics=TOPIC, subTopics=REC,
    prose="Write a recursive function that returns the sum of the digits of a whole "
          "number (no loops). Read a number and print the digit sum.",
    input_lines=["Line 1: A whole number"],
    inputs=["1234", "9", "9999", "0", "-45", "10", "999999"],
    solution="""
        def digit_sum(n):
            if n < 10:
                return n
            return n % 10 + digit_sum(n // 10)

        print(digit_sum(abs(int(input()))))
    """))

Q.append(dict(
    title="Recursive Power", difficulty="Hard", topics=TOPIC, subTopics=REC,
    prose="Write a recursive function that returns a raised to the power b (b is a "
          "non-negative whole number). Read a and b and print a to the power b.",
    input_lines=["Line 1: a, the base", "Line 2: b, the exponent"],
    inputs=["2\n10", "5\n0", "3\n4", "1\n5", "0\n5", "-2\n3", "10\n0"],
    solution="""
        def power(a, b):
            if b == 0:
                return 1
            return a * power(a, b - 1)

        base = int(input())
        exp = int(input())
        print(power(base, exp))
    """))

Q.append(dict(
    title="Recursive GCD", difficulty="Hard", topics=TOPIC, subTopics=REC,
    prose="Write a recursive function that returns the greatest common divisor of "
          "two numbers. Read two numbers and print their GCD.",
    input_lines=["Line 1: First number", "Line 2: Second number"],
    inputs=["12\n18", "17\n5", "100\n25", "1\n1", "0\n5", "7\n7", "1000\n999"],
    solution="""
        def gcd(a, b):
            if b == 0:
                return a
            return gcd(b, a % b)

        x = int(input())
        y = int(input())
        print(gcd(x, y))
    """))

Q.append(dict(
    title="Mini Calculator", difficulty="Hard", topics=TOPIC, subTopics=DEF,
    prose="Store the operations +, -, and * in a dictionary of lambdas. Read a "
          "number, an operator, and a second number, then print the result by "
          "looking up the operator.",
    input_lines=["Line 1: First number", "Line 2: An operator (+, -, or *)",
                 "Line 3: Second number"],
    inputs=["6\n+\n4", "10\n-\n3", "5\n*\n6", "0\n+\n0", "-5\n-\n-3", "1\n*\n1", "100\n+\n200"],
    solution="""
        ops = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
        }
        a = int(input())
        op = input()
        b = int(input())
        print(ops[op](a, b))
    """))

Q.append(dict(
    title="Multiplier Factory", difficulty="Hard", topics=TOPIC, subTopics=DEF,
    prose="Write a function make_multiplier(n) that returns a new function which "
          "multiplies its argument by n. Read a factor and a value, build the "
          "multiplier, and print the result of applying it to the value.",
    input_lines=["Line 1: The factor", "Line 2: The value"],
    inputs=["3\n5", "10\n10", "2\n7", "0\n5", "-3\n4", "1\n1", "100\n0"],
    solution="""
        def make_multiplier(n):
            def multiply(x):
                return n * x
            return multiply

        factor = int(input())
        value = int(input())
        times = make_multiplier(factor)
        print(times(value))
    """))

Q.append(dict(
    title="Sum of Even Squares", difficulty="Hard", topics=TOPIC, subTopics=DEF,
    prose="Read a line of numbers. Using filter to keep the even numbers and map to "
          "square them, print the sum of the squares of the even numbers.",
    input_lines=["Line 1: Space-separated numbers"],
    inputs=["1 2 3 4", "2 4 6", "1 3 5", "0", "-2 -4 3", "1 2 3 4 5 6 7 8", "10 -10 5"],
    solution="""
        nums = list(map(int, input().split()))
        evens = filter(lambda x: x % 2 == 0, nums)
        print(sum(map(lambda x: x * x, evens)))
    """))

Q.append(dict(
    title="Recursive String Reverse", difficulty="Hard", topics=TOPIC, subTopics=REC,
    prose="Write a recursive function that returns a string reversed (no loops and "
          "no slicing tricks other than peeling one character at a time). Read a "
          "word and print it reversed.",
    input_lines=["Line 1: A word"],
    inputs=["hello", "a", "abcde", "ab", "racecar", "z", "supercalifragilistic"],
    solution="""
        def reverse(s):
            if len(s) <= 1:
                return s
            return reverse(s[1:]) + s[0]

        print(reverse(input()))
    """))

Q.append(dict(
    title="Recursive Palindrome", difficulty="Hard", topics=TOPIC, subTopics=REC,
    prose="Write a recursive function that returns whether a word is a palindrome. "
          "Read a word and print 'Yes' if it is a palindrome, otherwise 'No'.",
    input_lines=["Line 1: A word"],
    inputs=["racecar", "hello", "level", "a", "ab", "noon", "abcba"],
    solution="""
        def is_palindrome(s):
            if len(s) <= 1:
                return True
            return s[0] == s[-1] and is_palindrome(s[1:-1])

        print("Yes" if is_palindrome(input()) else "No")
    """))

if __name__ == "__main__":
    out = os.path.abspath(os.path.join(
        os.path.dirname(__file__), "..",
        "Unit 8 - Functions",
        "Unit 8 - Functions - Coding Questions.xlsx"))
    os.makedirs(os.path.dirname(out), exist_ok=True)
    main(Q, out)
