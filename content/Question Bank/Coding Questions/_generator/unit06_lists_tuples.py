"""Unit 6 - Lists and Tuples - Coding Questions (30: 10/10/10).

Scope: list creation/indexing/slicing, mutating & methods, sorting,
list comprehensions, tuples & unpacking, nested lists, iterating.
"""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from cqlib import main

TOPIC = "lists"
OPS, COMP, TUP, NEST = "list-operations", "list-comprehensions", "tuples", "nested-lists"

Q = []

# ----------------------------- EASY (10) -----------------------------
Q.append(dict(
    title="Cart Total", difficulty="Easy", topics=TOPIC, subTopics=OPS,
    prose="An online cart adds up the prices of the items in it. Read a line of "
          "space-separated prices and print their total.",
    input_lines=["Line 1: Space-separated prices"],
    inputs=["10 20 30 40 50", "10", "-1 -2 3", "0", "0 0 0", "-5 -10 -15", "1 2 3 4 5 6 7 8 9 10"],
    solution="""
        prices = list(map(int, input().split()))
        print(sum(prices))
    """))

Q.append(dict(
    title="Item Count", difficulty="Easy", topics=TOPIC, subTopics=OPS,
    prose="Read a line of space-separated values and print how many values there "
          "are.",
    input_lines=["Line 1: Space-separated values"],
    inputs=["3 1 4 1 5", "42", "7 8 9 10", "a", "1 2 3 4 5 6 7 8 9 10", "x x x", "a b c d e f g h i j k l m n o"],
    solution="""
        items = input().split()
        print(len(items))
    """))

Q.append(dict(
    title="Most Expensive", difficulty="Easy", topics=TOPIC, subTopics=OPS,
    prose="Read a line of space-separated prices and print the largest one.",
    input_lines=["Line 1: Space-separated prices"],
    inputs=["10 55 30", "7", "-1 -9 -3", "0", "5 5 5", "-100 100 0", "1 2 3 4 5 6 7 8 9 10"],
    solution="""
        prices = list(map(int, input().split()))
        print(max(prices))
    """))

Q.append(dict(
    title="Cheapest", difficulty="Easy", topics=TOPIC, subTopics=OPS,
    prose="Read a line of space-separated prices and print the smallest one.",
    input_lines=["Line 1: Space-separated prices"],
    inputs=["10 55 30", "7", "-1 -9 -3", "0", "5 5 5", "-100 100 0", "1 2 3 4 5 6 7 8 9 10"],
    solution="""
        prices = list(map(int, input().split()))
        print(min(prices))
    """))

Q.append(dict(
    title="First Three", difficulty="Easy", topics=TOPIC, subTopics=OPS,
    prose="A leaderboard shows only the top three entries. Read a line of "
          "space-separated values and print the first three, separated by spaces "
          "(or all of them if there are fewer than three).",
    input_lines=["Line 1: Space-separated values"],
    inputs=["1 2 3 4 5", "9 8", "7", "a b c", "x", "1 2", "a b c d e f g h"],
    solution="""
        items = input().split()
        print(*items[:3])
    """))

Q.append(dict(
    title="Last Item", difficulty="Easy", topics=TOPIC, subTopics=OPS,
    prose="Read a line of space-separated values and print the last one.",
    input_lines=["Line 1: Space-separated values"],
    inputs=["apple banana cherry", "solo", "1 2 3", "a", "1 2 3 4 5", "x y", "a b c d e f g h i j"],
    solution="""
        items = input().split()
        print(items[-1])
    """))

Q.append(dict(
    title="Reversed List", difficulty="Easy", topics=TOPIC, subTopics=OPS,
    prose="Read a line of space-separated values and print them in reverse order, "
          "separated by spaces.",
    input_lines=["Line 1: Space-separated values"],
    inputs=["1 2 3 4", "a b c", "solo", "a b", "1 2 3 4 5 6 7 8", "x", "one two three four five"],
    solution="""
        items = input().split()
        print(*items[::-1])
    """))

Q.append(dict(
    title="Sorted List", difficulty="Easy", topics=TOPIC, subTopics=OPS,
    prose="Read a line of space-separated numbers and print them sorted from "
          "smallest to largest, separated by spaces.",
    input_lines=["Line 1: Space-separated numbers"],
    inputs=["3 1 4 1 5", "10 -2 7", "5", "0", "-3 -1 -2", "5 5 5 5", "9 8 7 6 5 4 3 2 1 0"],
    solution="""
        nums = list(map(int, input().split()))
        print(*sorted(nums))
    """))

Q.append(dict(
    title="Count a Value", difficulty="Easy", topics=TOPIC, subTopics=OPS,
    prose="Read a line of space-separated values, then a value to look for, and "
          "print how many times it appears in the list.",
    input_lines=["Line 1: Space-separated values", "Line 2: The value to count"],
    inputs=["1 2 2 3 2\n2", "a b c\nz", "5 5 5\n5", "a\na", "1 1 1 1 1\n1", "x y z\nx", "a b a b a b a\nb"],
    solution="""
        items = input().split()
        target = input()
        print(items.count(target))
    """))

Q.append(dict(
    title="Is It There?", difficulty="Easy", topics=TOPIC, subTopics=OPS,
    prose="Read a line of space-separated values, then a value. Print 'Yes' if the "
          "value is in the list, otherwise print 'No'.",
    input_lines=["Line 1: Space-separated values", "Line 2: The value to find"],
    inputs=["apple banana cherry\nbanana", "1 2 3\n9", "x y z\nx", "a\na", "1 2 3\n1", "a b c\nz", "one two three four five\nfour"],
    solution="""
        items = input().split()
        target = input()
        print("Yes" if target in items else "No")
    """))

# ----------------------------- MEDIUM (10) -----------------------------
Q.append(dict(
    title="Top Scores First", difficulty="Medium", topics=TOPIC, subTopics=OPS,
    prose="Read a line of space-separated scores and print them sorted from highest "
          "to lowest, separated by spaces.",
    input_lines=["Line 1: Space-separated scores"],
    inputs=["3 1 4 1 5", "10 20", "7", "0", "-5 -1 -10", "5 5 5", "9 3 7 1 8 2 6 4 0 5"],
    solution="""
        nums = list(map(int, input().split()))
        print(*sorted(nums, reverse=True))
    """))

Q.append(dict(
    title="Unique Items", difficulty="Medium", topics=TOPIC, subTopics=OPS,
    prose="Read a line of space-separated values and print each distinct value once, "
          "keeping the order of first appearance, separated by spaces.",
    input_lines=["Line 1: Space-separated values"],
    inputs=["a b a c b a", "1 1 1", "x y z", "a", "1 2 1 2 1 2", "z z z z z", "a b c a b c a b c d"],
    solution="""
        items = input().split()
        seen = []
        for x in items:
            if x not in seen:
                seen.append(x)
        print(*seen)
    """))

Q.append(dict(
    title="Runner-Up Score", difficulty="Medium", topics=TOPIC, subTopics=OPS,
    prose="Read a line of space-separated scores and print the second-highest "
          "distinct score.",
    input_lines=["Line 1: Space-separated scores (at least two distinct values)"],
    inputs=["3 1 4 1 5 9", "1 2", "5 5 4", "0 1", "-1 -2 -3", "10 10 9", "100 90 80 70 60"],
    solution="""
        nums = list(map(int, input().split()))
        distinct = sorted(set(nums), reverse=True)
        print(distinct[1])
    """))

Q.append(dict(
    title="Square Them", difficulty="Medium", topics=TOPIC, subTopics=COMP,
    prose="Read a line of space-separated numbers and print each number squared, in "
          "the same order, separated by spaces. Use a list comprehension.",
    input_lines=["Line 1: Space-separated numbers"],
    inputs=["1 2 3", "5", "-2 4", "0", "-1 -2 -3", "10 10 10", "1 2 3 4 5 6 7 8 9 10"],
    solution="""
        nums = list(map(int, input().split()))
        squares = [x * x for x in nums]
        print(*squares)
    """))

Q.append(dict(
    title="Keep the Evens", difficulty="Medium", topics=TOPIC, subTopics=COMP,
    prose="Read a line of space-separated numbers and print only the even ones, in "
          "the same order, separated by spaces. Use a list comprehension.",
    input_lines=["Line 1: Space-separated numbers"],
    inputs=["1 2 3 4 5 6", "2 3 4", "10 15 20", "0", "1 3 5 7", "-2 -4 -1", "1 2 3 4 5 6 7 8 9 10"],
    solution="""
        nums = list(map(int, input().split()))
        evens = [x for x in nums if x % 2 == 0]
        print(*evens)
    """))

Q.append(dict(
    title="Even-Index Sum", difficulty="Medium", topics=TOPIC, subTopics=OPS,
    prose="Read a line of space-separated numbers and print the sum of the values "
          "at the even positions 0, 2, 4, and so on.",
    input_lines=["Line 1: Space-separated numbers"],
    inputs=["10 20 30 40 50", "5", "1 2 3 4", "0", "-1 -2 -3 -4 -5", "1 1 1 1 1 1", "1 2 3 4 5 6 7 8 9 10"],
    solution="""
        nums = list(map(int, input().split()))
        print(sum(nums[::2]))
    """))

Q.append(dict(
    title="Rotate Right by One", difficulty="Medium", topics=TOPIC, subTopics=OPS,
    prose="Read a line of space-separated values and print them rotated one place to "
          "the right, so the last value moves to the front.",
    input_lines=["Line 1: Space-separated values"],
    inputs=["1 2 3 4", "5", "a b", "a", "1 2 3 4 5 6 7 8", "x y z", "a b c d e f g h i j"],
    solution="""
        items = input().split()
        rotated = items[-1:] + items[:-1]
        print(*rotated)
    """))

Q.append(dict(
    title="Merge and Sort", difficulty="Medium", topics=TOPIC, subTopics=OPS,
    prose="Read two lines, each a set of space-separated numbers. Combine them into "
          "one list, sort it from smallest to largest, and print it.",
    input_lines=["Line 1: First set of numbers", "Line 2: Second set of numbers"],
    inputs=["3 1\n4 2", "5\n1", "2 2\n1 1", "0\n0", "-1 -2\n1 2", "5 5 5\n5 5", "1 2 3 4 5\n6 7 8 9 10"],
    solution="""
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        print(*sorted(a + b))
    """))

Q.append(dict(
    title="Min and Max Pair", difficulty="Medium", topics=TOPIC, subTopics=TUP,
    prose="Read a line of space-separated numbers and print the smallest and "
          "largest as a pair in the form (min, max).",
    input_lines=["Line 1: Space-separated numbers"],
    inputs=["3 1 4 1 5", "7", "-1 -2 -3", "0", "5 5 5", "-100 0 100", "1 2 3 4 5 6 7 8 9 10"],
    solution="""
        nums = list(map(int, input().split()))
        pair = (min(nums), max(nums))
        print(f"({pair[0]}, {pair[1]})")
    """))

Q.append(dict(
    title="Position Finder", difficulty="Medium", topics=TOPIC, subTopics=OPS,
    prose="Read a line of space-separated numbers, then a target. Print the "
          "1-based position of the first time the target appears, or 0 if it does "
          "not appear.",
    input_lines=["Line 1: Space-separated numbers", "Line 2: The target"],
    inputs=["10 20 30\n20", "1 2 3\n5", "5 5 5\n5", "0\n0", "-1 -2 -3\n-2", "1 2 3 2 1\n2", "1 2 3 4 5 6 7 8 9 10\n10"],
    solution="""
        nums = list(map(int, input().split()))
        target = int(input())
        if target in nums:
            print(nums.index(target) + 1)
        else:
            print(0)
    """))

# ----------------------------- HARD (10) -----------------------------
Q.append(dict(
    title="Matrix Transpose", difficulty="Hard", topics=TOPIC, subTopics=NEST,
    prose="Read a grid with R rows and C columns, then print its transpose: the "
          "row/column roles swapped, C rows of R values each.",
    input_lines=["Line 1: R and C separated by a space",
                 "Next R lines: C space-separated numbers each"],
    inputs=["2 3\n1 2 3\n4 5 6", "1 1\n7", "2 2\n1 2\n3 4", "1 3\n1 2 3", "3 1\n1\n2\n3", "3 3\n1 2 3\n4 5 6\n7 8 9", "4 2\n1 2\n3 4\n5 6\n7 8"],
    solution="""
        r, c = map(int, input().split())
        grid = [list(map(int, input().split())) for _ in range(r)]
        for j in range(c):
            row = [grid[i][j] for i in range(r)]
            print(*row)
    """))

Q.append(dict(
    title="Column Sums", difficulty="Hard", topics=TOPIC, subTopics=NEST,
    prose="Read a grid with R rows and C columns and print the sum of each column "
          "on one line, separated by spaces.",
    input_lines=["Line 1: R and C separated by a space",
                 "Next R lines: C space-separated numbers each"],
    inputs=["2 3\n1 2 3\n4 5 6", "1 1\n7", "3 2\n1 1\n2 2\n3 3", "1 4\n1 2 3 4", "2 2\n-1 -2\n-3 -4", "4 1\n1\n2\n3\n4", "3 3\n1 2 3\n4 5 6\n7 8 9"],
    solution="""
        r, c = map(int, input().split())
        grid = [list(map(int, input().split())) for _ in range(r)]
        sums = [sum(grid[i][j] for i in range(r)) for j in range(c)]
        print(*sums)
    """))

Q.append(dict(
    title="Flatten the Rows", difficulty="Hard", topics=TOPIC, subTopics=NEST,
    prose="Read R rows, each a line of space-separated numbers of any length, and "
          "print all the numbers on a single line, separated by spaces, in order.",
    input_lines=["Line 1: R, the number of rows",
                 "Next R lines: space-separated numbers each"],
    inputs=["2\n1 2\n3 4 5", "1\n9", "3\n1\n2\n3", "0", "1\n1 2 3 4 5 6 7", "4\n1\n2 3\n4 5 6\n7", "2\n1 2 3 4 5\n6 7 8 9 10"],
    solution="""
        r = int(input())
        flat = []
        for _ in range(r):
            flat += input().split()
        print(*flat)
    """))

Q.append(dict(
    title="Diagonal Sum", difficulty="Hard", topics=TOPIC, subTopics=NEST,
    prose="Read a square grid of size N and print the sum of the values on its main "
          "diagonal (top-left to bottom-right).",
    input_lines=["Line 1: N",
                 "Next N lines: N space-separated numbers each"],
    inputs=["3\n1 2 3\n4 5 6\n7 8 9", "1\n5", "2\n1 2\n3 4", "1\n0", "4\n1 0 0 0\n0 2 0 0\n0 0 3 0\n0 0 0 4", "2\n-1 -2\n-3 -4", "5\n1 2 3 4 5\n6 7 8 9 10\n11 12 13 14 15\n16 17 18 19 20\n21 22 23 24 25"],
    solution="""
        n = int(input())
        grid = [list(map(int, input().split())) for _ in range(n)]
        total = sum(grid[i][i] for i in range(n))
        print(total)
    """))

Q.append(dict(
    title="Sort by Marks", difficulty="Hard", topics=TOPIC, subTopics=TUP,
    prose="Read N students, each on a line with a name and a score. Print the names "
          "in order from highest score to lowest. Keep the original order for "
          "students who tie.",
    input_lines=["Line 1: N", "Next N lines: 'name score'"],
    inputs=["3\nasha 80\nkabir 95\nmeera 70", "1\nsam 50", "2\na 10\nb 10", "0", "4\na 0\nb 100\nc 50\nd 50", "2\nx -5\ny -10", "5\np 60\nq 60\nr 90\ns 30\nt 90"],
    solution="""
        n = int(input())
        students = []
        for _ in range(n):
            name, score = input().split()
            students.append((name, int(score)))
        students.sort(key=lambda t: -t[1])
        for name, score in students:
            print(name)
    """))

Q.append(dict(
    title="Row Maximums", difficulty="Hard", topics=TOPIC, subTopics=NEST,
    prose="Read a grid with R rows and C columns and print the largest value in "
          "each row, one per line, top to bottom.",
    input_lines=["Line 1: R and C separated by a space",
                 "Next R lines: C space-separated numbers each"],
    inputs=["2 3\n1 9 3\n4 2 8", "1 1\n7", "2 2\n-1 -2\n-3 -4", "1 4\n1 2 3 4", "3 1\n5\n2\n8", "2 2\n0 0\n0 0", "4 3\n1 2 3\n4 5 6\n7 8 9\n10 11 12"],
    solution="""
        r, c = map(int, input().split())
        for _ in range(r):
            row = list(map(int, input().split()))
            print(max(row))
    """))

Q.append(dict(
    title="Value Counts", difficulty="Hard", topics=TOPIC, subTopics=OPS,
    prose="Read a line of space-separated numbers and, for each distinct value in "
          "ascending order, print the value and how many times it appears in the "
          "form 'value:count', one per line.",
    input_lines=["Line 1: Space-separated numbers"],
    inputs=["1 2 2 3 3 3", "5 5", "3 1 2", "0", "-1 -1 -2", "7 7 7 7 7", "1 2 3 4 5 6 7 8 9 10"],
    solution="""
        nums = list(map(int, input().split()))
        for v in sorted(set(nums)):
            print(f"{v}:{nums.count(v)}")
    """))

Q.append(dict(
    title="Two-Sum Positions", difficulty="Hard", topics=TOPIC, subTopics=NEST,
    prose="Read a line of space-separated numbers and a target. Print the 1-based "
          "positions of the first pair of values (earlier position first) that add "
          "up to the target, separated by a space. Print 'None' if there is no "
          "such pair.",
    input_lines=["Line 1: Space-separated numbers", "Line 2: Target"],
    inputs=["2 7 11 15\n9", "1 2 3\n7", "3 3\n6", "0 0\n0", "-1 -2 -3\n-5", "5 5 5 5\n10", "1 2 3 4 5 6 7 8 9 10\n19"],
    solution="""
        nums = list(map(int, input().split()))
        target = int(input())
        found = None
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    found = (i + 1, j + 1)
                    break
            if found:
                break
        print(f"{found[0]} {found[1]}" if found else "None")
    """))

Q.append(dict(
    title="Adjacent Products", difficulty="Hard", topics=TOPIC, subTopics=COMP,
    prose="Read a line of space-separated numbers and print the product of each "
          "adjacent pair, in order, separated by spaces. For '1 2 3 4' the answer "
          "is '2 6 12'.",
    input_lines=["Line 1: Space-separated numbers (at least two)"],
    inputs=["1 2 3 4", "2 5", "3 3 3", "0 0", "-1 -2 -3", "1 1 1 1 1", "1 2 3 4 5 6 7 8 9 10"],
    solution="""
        nums = list(map(int, input().split()))
        products = [nums[i] * nums[i + 1] for i in range(len(nums) - 1)]
        print(*products)
    """))

Q.append(dict(
    title="Common Elements", difficulty="Hard", topics=TOPIC, subTopics=OPS,
    prose="Read two lines of space-separated values. Print the values that appear "
          "in both lists, in the order they appear in the first list, separated by "
          "spaces (each common value once).",
    input_lines=["Line 1: First list", "Line 2: Second list"],
    inputs=["1 2 3 4\n2 4 6", "5 6 7\n6 7 8", "1 2\n2 1", "a\na", "1 2 3\n4 5 6", "x x y y\ny x", "1 2 3 4 5 6 7 8 9 10\n2 4 6 8 10 12"],
    solution="""
        a = input().split()
        b = input().split()
        result = []
        for x in a:
            if x in b and x not in result:
                result.append(x)
        print(*result)
    """))

if __name__ == "__main__":
    out = os.path.abspath(os.path.join(
        os.path.dirname(__file__), "..",
        "Unit 6 - Lists and Tuples",
        "Unit 6 - Lists and Tuples - Coding Questions.xlsx"))
    os.makedirs(os.path.dirname(out), exist_ok=True)
    main(Q, out)
