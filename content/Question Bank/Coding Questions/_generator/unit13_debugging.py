"""Unit 13 - Debugging - Coding Questions (30: 10/10/10).

Scope maps the unit's ideas onto write-the-correct-program tasks: getting
boundaries and off-by-one cases right, handling negatives, and using assert for
sanity checks / invariants. Every reference solution is the bug-free version.
"""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from cqlib import main

TOPIC = "debugging"
EDGE, ASSERT, VAL = "edge-cases", "assertions", "validation"

Q = []

# ----------------------------- EASY (10) -----------------------------
Q.append(dict(
    title="Inclusive Count", difficulty="Easy", topics=TOPIC, subTopics=EDGE,
    prose="A common off-by-one bug: count how many whole numbers there are from A to "
          "B, including both ends. Read A and B and print the count.",
    input_lines=["Line 1: 'A B'"],
    inputs=["1 5", "3 3", "0 9", "-5 -1", "-3 3", "0 0", "10 20"],
    solution="""
        a, b = map(int, input().split())
        print(b - a + 1)
    """))

Q.append(dict(
    title="Sum of Inclusive Range", difficulty="Easy", topics=TOPIC, subTopics=EDGE,
    prose="Read A and B and print the sum of every whole number from A to B, "
          "including both A and B.",
    input_lines=["Line 1: 'A B'"],
    inputs=["1 5", "3 3", "1 10", "-5 -1", "-3 3", "0 0", "10 20"],
    solution="""
        a, b = map(int, input().split())
        print(sum(range(a, b + 1)))
    """))

Q.append(dict(
    title="Last Valid Index", difficulty="Easy", topics=TOPIC, subTopics=EDGE,
    prose="A list of length n has valid indexes 0 to n-1. Read a line of values and "
          "print the last valid index.",
    input_lines=["Line 1: Space-separated values"],
    inputs=["1 2 3", "5", "1 2 3 4", "0", "-1 -2", "1 2 3 4 5 6", "a b c d"],
    solution="""
        items = input().split()
        print(len(items) - 1)
    """))

Q.append(dict(
    title="Assert Non-Zero", difficulty="Easy", topics=TOPIC, subTopics=ASSERT,
    prose="Read two numbers. Use an assert to confirm the second is not zero (a "
          "sanity check), then print the first divided by the second.",
    input_lines=["Line 1: 'a b' (b is never zero)"],
    inputs=["10 2", "9 3", "8 4", "0 5", "-10 2", "1 1", "-9 3"],
    solution="""
        a, b = map(int, input().split())
        assert b != 0, "divisor must be non-zero"
        print(a / b)
    """))

Q.append(dict(
    title="Boundary Pass Mark", difficulty="Easy", topics=TOPIC, subTopics=EDGE,
    prose="The pass mark is 40 and exactly 40 passes. Read a score and print 'Pass' "
          "if it is 40 or more, otherwise 'Fail'.",
    input_lines=["Line 1: A score"],
    inputs=["40", "39", "100", "0", "41", "-5", "1000"],
    solution="""
        score = int(input())
        print("Pass" if score >= 40 else "Fail")
    """))

Q.append(dict(
    title="Correct Average", difficulty="Easy", topics=TOPIC, subTopics=EDGE,
    prose="A buggy average often uses integer division by mistake. Read a line of "
          "numbers and print their true average rounded to 2 decimal places.",
    input_lines=["Line 1: Space-separated numbers"],
    inputs=["1 2", "3", "2 4 6", "0", "-3 3", "1 1 1 1", "-10 -20"],
    solution="""
        nums = list(map(int, input().split()))
        print(round(sum(nums) / len(nums), 2))
    """))

Q.append(dict(
    title="Count Up Correctly", difficulty="Easy", topics=TOPIC, subTopics=EDGE,
    prose="Print every number from 1 to N, including N, separated by spaces (getting "
          "the loop bounds right).",
    input_lines=["Line 1: N"],
    inputs=["5", "1", "3", "0", "2", "10", "7"],
    solution="""
        n = int(input())
        print(*range(1, n + 1))
    """))

Q.append(dict(
    title="Equal or Larger", difficulty="Easy", topics=TOPIC, subTopics=EDGE,
    prose="Read two numbers. Print 'Equal' if they are equal; otherwise print the "
          "larger one. (Watch the boundary where they are equal.)",
    input_lines=["Line 1: 'a b'"],
    inputs=["3 3", "5 2", "1 4", "0 0", "-5 -5", "-1 1", "100 99"],
    solution="""
        a, b = map(int, input().split())
        if a == b:
            print("Equal")
        else:
            print(max(a, b))
    """))

Q.append(dict(
    title="Even Check", difficulty="Easy", topics=TOPIC, subTopics=EDGE,
    prose="Read a number and print 'Even' or 'Odd'. Remember that 0 is even.",
    input_lines=["Line 1: A number"],
    inputs=["4", "7", "0", "-4", "-7", "1", "1000000"],
    solution="""
        n = int(input())
        print("Even" if n % 2 == 0 else "Odd")
    """))

Q.append(dict(
    title="Assert Non-Empty", difficulty="Easy", topics=TOPIC, subTopics=ASSERT,
    prose="Read a word. Use an assert to confirm it is not empty, then print its "
          "first character.",
    input_lines=["Line 1: A non-empty word"],
    inputs=["hello", "a", "xyz", "Z", "world", "1", "banana"],
    solution="""
        word = input()
        assert len(word) > 0, "word must not be empty"
        print(word[0])
    """))

# ----------------------------- MEDIUM (10) -----------------------------
Q.append(dict(
    title="Max Including Negatives", difficulty="Medium", topics=TOPIC, subTopics=EDGE,
    prose="A classic bug initialises the maximum to 0, which fails when all values "
          "are negative. Read a line of numbers and print the true maximum.",
    input_lines=["Line 1: Space-separated numbers"],
    inputs=["-3 -1 -2", "5 3 9", "-7", "0", "-100 -1 -50", "1 2 3 4 5",
            "-5 5 -5 5"],
    solution="""
        nums = list(map(int, input().split()))
        largest = nums[0]
        for x in nums[1:]:
            if x > largest:
                largest = x
        print(largest)
    """))

Q.append(dict(
    title="Correct Percentage", difficulty="Medium", topics=TOPIC, subTopics=EDGE,
    prose="Read marks obtained and the total marks, and print the percentage rounded "
          "to 1 decimal place (avoiding the integer-division bug).",
    input_lines=["Line 1: 'obtained total'"],
    inputs=["45 50", "1 3", "50 50", "0 50", "50 200", "1 1", "33 99"],
    solution="""
        obtained, total = map(int, input().split())
        print(round(obtained / total * 100, 1))
    """))

Q.append(dict(
    title="Grade Boundaries", difficulty="Medium", topics=TOPIC, subTopics=EDGE,
    prose="Read a mark and print its grade using inclusive boundaries: 'A' for 90 or "
          "more, 'B' for 75 or more, 'C' for 60 or more, and 'F' otherwise. Check "
          "the exact boundary values.",
    input_lines=["Line 1: A mark"],
    inputs=["90", "75", "59", "60", "0", "100", "89"],
    solution="""
        marks = int(input())
        if marks >= 90:
            print("A")
        elif marks >= 75:
            print("B")
        elif marks >= 60:
            print("C")
        else:
            print("F")
    """))

Q.append(dict(
    title="Assert Sorted Search", difficulty="Medium", topics=TOPIC, subTopics=ASSERT,
    prose="Read a sorted line of numbers and a target. Use an assert to confirm the "
          "list really is sorted, then print 'Found' if the target is present and "
          "'Not Found' otherwise.",
    input_lines=["Line 1: Sorted space-separated numbers", "Line 2: Target"],
    inputs=["1 2 3 4 5\n3", "1 2 3\n9", "2 4 6\n6", "5\n5", "-3 -1 0 2\n-1",
            "1 2 3 4 5 6 7\n1", "-5 -4 -3\n-4"],
    solution="""
        nums = list(map(int, input().split()))
        assert nums == sorted(nums), "list must be sorted"
        target = int(input())
        print("Found" if target in nums else "Not Found")
    """))

Q.append(dict(
    title="Sum of Squares", difficulty="Medium", topics=TOPIC, subTopics=EDGE,
    prose="A buggy version adds the numbers instead of their squares. Read a line of "
          "numbers and print the sum of their squares.",
    input_lines=["Line 1: Space-separated numbers"],
    inputs=["1 2 3", "5", "2 4", "0", "-3 3", "-1 -2 -3", "10 20"],
    solution="""
        nums = list(map(int, input().split()))
        print(sum(x * x for x in nums))
    """))

Q.append(dict(
    title="Above Average Count", difficulty="Medium", topics=TOPIC, subTopics=EDGE,
    prose="Read a line of numbers and print how many of them are strictly greater "
          "than the average of the list.",
    input_lines=["Line 1: Space-separated numbers"],
    inputs=["1 2 3 4", "5 5 5", "1 10", "0", "-5 -1 5", "1 1 1 1 1", "100"],
    solution="""
        nums = list(map(int, input().split()))
        average = sum(nums) / len(nums)
        print(sum(1 for x in nums if x > average))
    """))

Q.append(dict(
    title="Palindrome Number", difficulty="Medium", topics=TOPIC, subTopics=EDGE,
    prose="Read a whole number and print 'Yes' if its digits read the same forwards "
          "and backwards, otherwise 'No'. A single-digit number counts as a "
          "palindrome.",
    input_lines=["Line 1: A whole number"],
    inputs=["121", "123", "7", "0", "1001", "12321", "10"],
    solution="""
        n = input().strip()
        print("Yes" if n == n[::-1] else "No")
    """))

Q.append(dict(
    title="Reverse Without Loss", difficulty="Medium", topics=TOPIC, subTopics=EDGE,
    prose="Read a line of values and print them reversed, making sure not to drop "
          "the first or last element.",
    input_lines=["Line 1: Space-separated values"],
    inputs=["1 2 3", "5", "1 2", "a", "1 2 3 4 5", "x y", "9 8 7 6"],
    solution="""
        items = input().split()
        print(*items[::-1])
    """))

Q.append(dict(
    title="Smallest Gap", difficulty="Medium", topics=TOPIC, subTopics=EDGE,
    prose="Read a line of numbers, sort them, and print the smallest difference "
          "between any two neighbouring values in the sorted order.",
    input_lines=["Line 1: Space-separated numbers (at least two)"],
    inputs=["3 1 4 1 5", "10 20 30", "5 8", "1 1", "-5 5", "-10 -3 -7", "0 0 0"],
    solution="""
        nums = sorted(map(int, input().split()))
        smallest = nums[1] - nums[0]
        for i in range(1, len(nums)):
            gap = nums[i] - nums[i - 1]
            if gap < smallest:
                smallest = gap
        print(smallest)
    """))

Q.append(dict(
    title="Assert Valid Marks", difficulty="Medium", topics=TOPIC, subTopics=ASSERT,
    prose="Read a line of marks. Use an assert to confirm every mark is between 0 "
          "and 100, then print their average rounded to 1 decimal place.",
    input_lines=["Line 1: Space-separated marks (each 0 to 100)"],
    inputs=["80 90 100", "50", "0 100", "0", "100", "1 2 3 4 5", "60 70 80 90"],
    solution="""
        marks = list(map(int, input().split()))
        assert all(0 <= m <= 100 for m in marks), "marks out of range"
        print(round(sum(marks) / len(marks), 1))
    """))

# ----------------------------- HARD (10) -----------------------------
Q.append(dict(
    title="Pair Sum Exists", difficulty="Hard", topics=TOPIC, subTopics=EDGE,
    prose="Read a sorted line of numbers and a target. Print 'Yes' if some pair of "
          "different positions adds up to the target, otherwise 'No'. Use two "
          "indexes moving inward and mind the boundaries.",
    input_lines=["Line 1: Sorted space-separated numbers", "Line 2: Target"],
    inputs=["1 2 3 4\n5", "1 2 3\n7", "2 4\n6", "1 2\n3", "-5 -1 0 3\n-6",
            "1 2 3 4 5 6\n11", "-3 -2 -1\n-3"],
    solution="""
        nums = list(map(int, input().split()))
        target = int(input())
        left, right = 0, len(nums) - 1
        found = False
        while left < right:
            total = nums[left] + nums[right]
            if total == target:
                found = True
                break
            elif total < target:
                left += 1
            else:
                right -= 1
        print("Yes" if found else "No")
    """))

Q.append(dict(
    title="Max Window Sum", difficulty="Hard", topics=TOPIC, subTopics=EDGE,
    prose="Read a line of numbers and a window size K. Print the largest sum of any "
          "K consecutive numbers. Take care that the last window is included.",
    input_lines=["Line 1: Space-separated numbers", "Line 2: K"],
    inputs=["1 2 3 4 5\n2", "5 1 1\n1", "2 2 2\n3", "-1 -2 -3\n1",
            "5\n1", "1 2 3 4\n4", "-5 10 -3 8\n2"],
    solution="""
        nums = list(map(int, input().split()))
        k = int(input())
        best = sum(nums[:k])
        for i in range(1, len(nums) - k + 1):
            window = sum(nums[i:i + k])
            if window > best:
                best = window
        print(best)
    """))

Q.append(dict(
    title="Careful Rounding", difficulty="Hard", topics=TOPIC, subTopics=EDGE,
    prose="Floating-point sums can look wrong (0.1 + 0.2 is not exactly 0.3). Read a "
          "line of decimal amounts and print their total rounded to 2 decimal "
          "places.",
    input_lines=["Line 1: Space-separated decimal numbers"],
    inputs=["0.1 0.2", "1.5 2.5", "0.01 0.02", "0.0", "-1.5 1.5", "10.999 0.001",
            "-0.1 -0.2"],
    solution="""
        amounts = list(map(float, input().split()))
        print(round(sum(amounts), 2))
    """))

Q.append(dict(
    title="Stack Invariant", difficulty="Hard", topics=TOPIC, subTopics=ASSERT,
    prose="Simulate a stack with N operations ('push' or 'pop'). Use an assert to "
          "guarantee you never pop an empty stack (the input is well-formed), then "
          "print the final number of items on the stack.",
    input_lines=["Line 1: N", "Next N lines: 'push' or 'pop'"],
    inputs=["4\npush\npush\npop\npush", "2\npush\npop", "3\npush\npush\npush",
            "0", "1\npush", "6\npush\npush\npop\npop\npush\npop",
            "5\npush\npop\npush\npop\npush"],
    solution="""
        n = int(input())
        size = 0
        for _ in range(n):
            op = input()
            if op == "push":
                size += 1
            else:
                assert size > 0, "cannot pop empty stack"
                size -= 1
        print(size)
    """))

Q.append(dict(
    title="Count All Vowels", difficulty="Hard", topics=TOPIC, subTopics=EDGE,
    prose="A buggy counter resets between words and loses the total. Read a sentence "
          "and print the total number of vowels across the whole sentence, ignoring "
          "case.",
    input_lines=["Line 1: A sentence"],
    inputs=["the quick brown", "aeiou", "xyz", "AEIOU", "b c d", "a", "Hello World"],
    solution="""
        sentence = input().lower()
        count = 0
        for ch in sentence:
            if ch in "aeiou":
                count += 1
        print(count)
    """))

Q.append(dict(
    title="First Repeated Value", difficulty="Hard", topics=TOPIC, subTopics=EDGE,
    prose="Read a line of numbers and print the first value whose second occurrence "
          "appears earliest as you scan left to right. If nothing repeats, print "
          "'None'.",
    input_lines=["Line 1: Space-separated numbers"],
    inputs=["1 2 3 2 1", "5 6 7", "4 4", "1", "1 1 1", "-3 -3", "9 8 7 6 8"],
    solution="""
        nums = input().split()
        seen = set()
        answer = "None"
        for x in nums:
            if x in seen:
                answer = x
                break
            seen.add(x)
        print(answer)
    """))

Q.append(dict(
    title="Max Subarray Sum", difficulty="Hard", topics=TOPIC, subTopics=EDGE,
    prose="Read a line of numbers (which may be negative) and print the largest sum "
          "of any run of one or more consecutive numbers.",
    input_lines=["Line 1: Space-separated numbers"],
    inputs=["-2 1 -3 4 -1 2 1 -5 4", "-1 -2 -3", "1 2 3", "0", "-5", "5",
            "-1 2 -1 2 -1"],
    solution="""
        nums = list(map(int, input().split()))
        best = current = nums[0]
        for x in nums[1:]:
            current = max(x, current + x)
            best = max(best, current)
        print(best)
    """))

Q.append(dict(
    title="Assert Then Factorial", difficulty="Hard", topics=TOPIC, subTopics=ASSERT,
    prose="Read a number. Use an assert to confirm it is not negative (factorial is "
          "undefined for negatives), then compute and print its factorial.",
    input_lines=["Line 1: A number"],
    inputs=["5", "0", "6", "1", "2", "10", "3"],
    solution="""
        n = int(input())
        assert n >= 0, "factorial needs a non-negative number"
        result = 1
        for i in range(2, n + 1):
            result *= i
        print(result)
    """))

Q.append(dict(
    title="Leap Year Rules", difficulty="Hard", topics=TOPIC, subTopics=VAL,
    prose="Implement the leap-year rules yourself (a common source of bugs): a year "
          "is a leap year if it is divisible by 4, except years divisible by 100 "
          "are not, unless they are also divisible by 400. Read a year and print "
          "'Yes' or 'No'.",
    input_lines=["Line 1: A year"],
    inputs=["2000", "1900", "2024", "2100", "1600", "2023", "0"],
    solution="""
        year = int(input())
        if year % 400 == 0:
            leap = True
        elif year % 100 == 0:
            leap = False
        elif year % 4 == 0:
            leap = True
        else:
            leap = False
        print("Yes" if leap else "No")
    """))

Q.append(dict(
    title="Collatz Steps", difficulty="Hard", topics=TOPIC, subTopics=EDGE,
    prose="Read a number and count how many steps it takes to reach 1 using the "
          "Collatz process: if the number is even, halve it; if odd, triple it and "
          "add one. Print the number of steps (0 if the number is already 1).",
    input_lines=["Line 1: A positive whole number"],
    inputs=["6", "1", "7", "2", "27", "100", "3"],
    solution="""
        n = int(input())
        steps = 0
        while n != 1:
            if n % 2 == 0:
                n //= 2
            else:
                n = 3 * n + 1
            steps += 1
        print(steps)
    """))

if __name__ == "__main__":
    out = os.path.abspath(os.path.join(
        os.path.dirname(__file__), "..",
        "Unit 13 - Debugging",
        "Unit 13 - Debugging - Coding Questions.xlsx"))
    os.makedirs(os.path.dirname(out), exist_ok=True)
    main(Q, out)
