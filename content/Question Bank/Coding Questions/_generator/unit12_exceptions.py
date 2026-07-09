"""Unit 12 - Exception Handling - Coding Questions (30: 10/10/10).

Scope: try/except, specific & multiple exceptions, else/finally, raise,
custom exceptions, defensive input validation.
"""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from cqlib import main

TOPIC = "exception-handling"
TRY, RAISE, VAL = "try-except", "raising-exceptions", "defensive-programming"

Q = []

# ----------------------------- EASY (10) -----------------------------
Q.append(dict(
    title="Safe Division", difficulty="Easy", topics=TOPIC, subTopics=TRY,
    prose="Read two whole numbers and print the first divided by the second using "
          "integer division. If the second number is zero, catch the error and "
          "print 'Cannot divide by zero'.",
    input_lines=["Line 1: First number", "Line 2: Second number"],
    inputs=["10\n2", "7\n0", "9\n3", "0\n5", "-10\n2", "1\n1", "-7\n0"],
    solution="""
        a = int(input())
        b = int(input())
        try:
            print(a // b)
        except ZeroDivisionError:
            print("Cannot divide by zero")
    """))

Q.append(dict(
    title="Safe Integer", difficulty="Easy", topics=TOPIC, subTopics=TRY,
    prose="Read a line and try to treat it as a whole number, printing double its "
          "value. If it is not a valid number, print 'Not a number'.",
    input_lines=["Line 1: A value"],
    inputs=["5", "abc", "-3", "0", "3.5", "\n", "999999"],
    solution="""
        text = input()
        try:
            print(int(text) * 2)
        except ValueError:
            print("Not a number")
    """))

Q.append(dict(
    title="Safe Index", difficulty="Easy", topics=TOPIC, subTopics=TRY,
    prose="Read a line of numbers and an index. Print the value at that index, or "
          "'Index out of range' if the index is too large.",
    input_lines=["Line 1: Space-separated numbers", "Line 2: An index"],
    inputs=["10 20 30\n1", "1 2 3\n5", "7\n0", "1 2 3\n-1", "1 2 3\n-10",
            "5 10 15 20\n3", "9\n1"],
    solution="""
        nums = input().split()
        i = int(input())
        try:
            print(nums[i])
        except IndexError:
            print("Index out of range")
    """))

Q.append(dict(
    title="Safe Key", difficulty="Easy", topics=TOPIC, subTopics=TRY,
    prose="Read N key/value pairs and a key. Print the value for that key, or 'Key "
          "not found' if it is missing. Use a try/except on the dictionary lookup.",
    input_lines=["Line 1: N", "Next N lines: 'key value'", "Last line: a key"],
    inputs=["2\na 1\nb 2\na", "1\nx 5\nz", "2\np 3\nq 4\nq", "0\nkey",
            "1\nz 9\nz", "3\na 1\nb 2\nc 3\nd", "1\nk 0\nk"],
    solution="""
        n = int(input())
        data = {}
        for _ in range(n):
            key, value = input().split()
            data[key] = value
        query = input()
        try:
            print(data[query])
        except KeyError:
            print("Key not found")
    """))

Q.append(dict(
    title="Safe Float", difficulty="Easy", topics=TOPIC, subTopics=TRY,
    prose="Read a line and try to treat it as a decimal number, printing it rounded "
          "to 2 decimal places. If it is not valid, print 'Invalid'.",
    input_lines=["Line 1: A value"],
    inputs=["3.14159", "hello", "2", "0", "-1.005", "\n", "1e10"],
    solution="""
        text = input()
        try:
            print(round(float(text), 2))
        except ValueError:
            print("Invalid")
    """))

Q.append(dict(
    title="Add Two Safely", difficulty="Easy", topics=TOPIC, subTopics=TRY,
    prose="Read two lines and print their sum as whole numbers. If either line is "
          "not a valid number, print 'Invalid input'.",
    input_lines=["Line 1: First value", "Line 2: Second value"],
    inputs=["3\n4", "x\n5", "10\n20", "0\n0", "-5\n5", "7\ny", "100\n200"],
    solution="""
        try:
            a = int(input())
            b = int(input())
            print(a + b)
        except ValueError:
            print("Invalid input")
    """))

Q.append(dict(
    title="Sum Valid Numbers", difficulty="Easy", topics=TOPIC, subTopics=TRY,
    prose="Read a line of tokens separated by spaces and print the sum of only the "
          "ones that are valid whole numbers, ignoring the rest.",
    input_lines=["Line 1: Space-separated tokens"],
    inputs=["1 2 x 3", "a b", "10 20 hi 30", "0", "-1 -2 3", "1 2 3 4",
            "x y z"],
    solution="""
        total = 0
        for token in input().split():
            try:
                total += int(token)
            except ValueError:
                pass
        print(total)
    """))

Q.append(dict(
    title="Safe Modulo", difficulty="Easy", topics=TOPIC, subTopics=TRY,
    prose="Read two whole numbers and print the remainder of the first divided by "
          "the second. If the second is zero, print 'Cannot mod by zero'.",
    input_lines=["Line 1: First number", "Line 2: Second number"],
    inputs=["10\n3", "5\n0", "8\n4", "0\n5", "-10\n3", "1\n1", "-8\n0"],
    solution="""
        a = int(input())
        b = int(input())
        try:
            print(a % b)
        except ZeroDivisionError:
            print("Cannot mod by zero")
    """))

Q.append(dict(
    title="Divide with Finally", difficulty="Easy", topics=TOPIC, subTopics=TRY,
    prose="Read two whole numbers and print the first divided by the second. If the "
          "second is zero, print 'Cannot divide'. Either way, print 'Done' at the "
          "end using a finally block.",
    input_lines=["Line 1: First number", "Line 2: Second number"],
    inputs=["10\n2", "5\n0", "6\n3", "0\n5", "-10\n2", "1\n1", "-6\n0"],
    solution="""
        a = int(input())
        b = int(input())
        try:
            print(a / b)
        except ZeroDivisionError:
            print("Cannot divide")
        finally:
            print("Done")
    """))

Q.append(dict(
    title="Safe Square Root", difficulty="Easy", topics=TOPIC, subTopics=TRY,
    prose="Read a number and print its square root. If the number is negative, the "
          "square root fails, so catch the error and print 'Cannot take square root "
          "of negative'.",
    input_lines=["Line 1: A number"],
    inputs=["16", "-4", "9", "0", "-1", "1", "100"],
    solution="""
        import math
        n = int(input())
        try:
            print(math.sqrt(n))
        except ValueError:
            print("Cannot take square root of negative")
    """))

# ----------------------------- MEDIUM (10) -----------------------------
Q.append(dict(
    title="Two Kinds of Errors", difficulty="Medium", topics=TOPIC, subTopics=TRY,
    prose="Read two lines and divide the first by the second. Print 'Zero' if the "
          "second is zero and 'Invalid' if either value is not a number; otherwise "
          "print the result.",
    input_lines=["Line 1: First value", "Line 2: Second value"],
    inputs=["10\n2", "5\n0", "x\n3", "0\n5", "-10\n2", "7\ny", "1\n1"],
    solution="""
        try:
            a = int(input())
            b = int(input())
            print(a / b)
        except ZeroDivisionError:
            print("Zero")
        except ValueError:
            print("Invalid")
    """))

Q.append(dict(
    title="Else and Finally", difficulty="Medium", topics=TOPIC, subTopics=TRY,
    prose="Read two numbers and divide them. Use an else block to print the result "
          "when it works, an except block to print 'Error' on divide-by-zero, and a "
          "finally block that always prints 'Checked'.",
    input_lines=["Line 1: First number", "Line 2: Second number"],
    inputs=["8\n2", "9\n0", "10\n5", "0\n5", "-8\n2", "1\n1", "-9\n0"],
    solution="""
        a = int(input())
        b = int(input())
        try:
            result = a / b
        except ZeroDivisionError:
            print("Error")
        else:
            print(result)
        finally:
            print("Checked")
    """))

Q.append(dict(
    title="Validate Age", difficulty="Medium", topics=TOPIC, subTopics=RAISE,
    prose="Read an age. Write code that raises a ValueError if the age is below 0 or "
          "above 150, then catch it and print 'Invalid age'. Otherwise print 'Valid "
          "age'.",
    input_lines=["Line 1: An age"],
    inputs=["25", "-5", "200", "0", "150", "151", "1"],
    solution="""
        age = int(input())
        try:
            if age < 0 or age > 150:
                raise ValueError("bad age")
            print("Valid age")
        except ValueError:
            print("Invalid age")
    """))

Q.append(dict(
    title="Custom Exception", difficulty="Medium", topics=TOPIC, subTopics=RAISE,
    prose="Define a custom exception called NegativeError. Read a number and raise "
          "NegativeError if it is negative; catch it and print 'Negative not "
          "allowed'. Otherwise print the number's square.",
    input_lines=["Line 1: A number"],
    inputs=["5", "-3", "4", "0", "-1", "10", "-100"],
    solution="""
        class NegativeError(Exception):
            pass

        n = int(input())
        try:
            if n < 0:
                raise NegativeError()
            print(n * n)
        except NegativeError:
            print("Negative not allowed")
    """))

Q.append(dict(
    title="Range Validator", difficulty="Medium", topics=TOPIC, subTopics=VAL,
    prose="Read a value, then a minimum and maximum. Raise and catch a ValueError to "
          "print 'In range' if the value is between them (inclusive) and 'Out of "
          "range' otherwise.",
    input_lines=["Line 1: The value", "Line 2: 'min max'"],
    inputs=["5\n1 10", "15\n1 10", "7\n0 7", "0\n0 7", "-1\n0 7", "10\n1 10",
            "-5\n-10 -1"],
    solution="""
        value = int(input())
        low, high = map(int, input().split())
        try:
            if not (low <= value <= high):
                raise ValueError()
            print("In range")
        except ValueError:
            print("Out of range")
    """))

Q.append(dict(
    title="First Valid Number", difficulty="Medium", topics=TOPIC, subTopics=TRY,
    prose="Read N lines and print the first one that is a valid whole number. If "
          "none of them are, print 'No valid number'.",
    input_lines=["Line 1: N", "Next N lines: values"],
    inputs=["3\nabc\n12\nxyz", "2\nx\ny", "2\n5\n6", "0", "1\nabc",
            "3\nx\ny\n0", "4\na\nb\nc\n-5"],
    solution="""
        n = int(input())
        answer = "No valid number"
        for _ in range(n):
            line = input()
            try:
                answer = int(line)
                break
            except ValueError:
                continue
        print(answer)
    """))

Q.append(dict(
    title="Safe Nested Lookup", difficulty="Medium", topics=TOPIC, subTopics=TRY,
    prose="Read a line of JSON and print the value at data['user']['name']. If any "
          "part of that path is missing, print 'Not available'.",
    input_lines=["Line 1: A JSON object"],
    inputs=['{"user": {"name": "Asha"}}', '{"user": {}}', "{}",
            '{"user": {"name": ""}}', '{"other": 1}',
            '{"user": {"name": "Kabir", "age": 20}}', '{"x": 1, "y": 2}'],
    solution="""
        import json
        data = json.loads(input())
        try:
            print(data["user"]["name"])
        except KeyError:
            print("Not available")
    """))

Q.append(dict(
    title="Index or Bad Input", difficulty="Medium", topics=TOPIC, subTopics=TRY,
    prose="Read a line of numbers and an index. Print the value at that index, "
          "'Invalid index' if the index is not a number, or 'Out of range' if it is "
          "too large.",
    input_lines=["Line 1: Space-separated numbers", "Line 2: An index"],
    inputs=["10 20 30\n1", "1 2 3\nx", "1 2 3\n9", "1 2 3\n0", "1 2 3\n-1",
            "5\ny", "1 2 3 4\n3"],
    solution="""
        nums = input().split()
        raw = input()
        try:
            i = int(raw)
            print(nums[i])
        except ValueError:
            print("Invalid index")
        except IndexError:
            print("Out of range")
    """))

Q.append(dict(
    title="Divide the List", difficulty="Medium", topics=TOPIC, subTopics=TRY,
    prose="Read a line of numbers and a divisor. Print each number divided by the "
          "divisor (integer division), separated by spaces. If the divisor is zero, "
          "print 'Cannot divide' instead.",
    input_lines=["Line 1: Space-separated numbers", "Line 2: The divisor"],
    inputs=["10 20 30\n2", "5 6\n0", "9\n3", "0\n5", "-10 -20\n2", "1\n1",
            "-9\n0"],
    solution="""
        nums = list(map(int, input().split()))
        divisor = int(input())
        try:
            result = [n // divisor for n in nums]
            print(*result)
        except ZeroDivisionError:
            print("Cannot divide")
    """))

Q.append(dict(
    title="Safe Average", difficulty="Medium", topics=TOPIC, subTopics=TRY,
    prose="Read N, then N numbers on separate lines, and print their average. If N "
          "is zero there is no data, so catch the division error and print 'No "
          "data'.",
    input_lines=["Line 1: N", "Next N lines: one number each"],
    inputs=["3\n10\n20\n30", "0", "1\n50", "2\n-5\n5", "1\n0",
            "4\n1\n2\n3\n4", "2\n100\n200"],
    solution="""
        n = int(input())
        nums = [int(input()) for _ in range(n)]
        try:
            print(sum(nums) / len(nums))
        except ZeroDivisionError:
            print("No data")
    """))

# ----------------------------- HARD (10) -----------------------------
Q.append(dict(
    title="Insufficient Funds", difficulty="Hard", topics=TOPIC, subTopics=RAISE,
    prose="Define a custom InsufficientFunds exception. Read a starting balance and "
          "N operations ('deposit X' or 'withdraw X'); a withdrawal beyond the "
          "balance raises the exception. After each operation print the new "
          "balance, or 'Insufficient funds' if a withdrawal was refused.",
    input_lines=["Line 1: Starting balance", "Line 2: N",
                 "Next N lines: 'deposit X' or 'withdraw X'"],
    inputs=["100\n2\nwithdraw 50\nwithdraw 100", "0\n1\ndeposit 30",
            "50\n1\nwithdraw 60", "0\n1\nwithdraw 1", "10\n1\nwithdraw 10",
            "5\n3\ndeposit 5\nwithdraw 100\nwithdraw 10",
            "0\n0"],
    solution="""
        class InsufficientFunds(Exception):
            pass

        balance = int(input())
        n = int(input())
        for _ in range(n):
            op, amount = input().split()
            amount = int(amount)
            try:
                if op == "withdraw":
                    if amount > balance:
                        raise InsufficientFunds()
                    balance -= amount
                else:
                    balance += amount
                print(balance)
            except InsufficientFunds:
                print("Insufficient funds")
    """))

Q.append(dict(
    title="Validate Registration", difficulty="Hard", topics=TOPIC, subTopics=VAL,
    prose="Read a name, an age, and an email. Validate in order: the name must not "
          "be empty, the age must be a whole number from 1 to 120, and the email "
          "must contain '@'. Print 'Valid' if all pass, otherwise print the first "
          "failure: 'Invalid name', 'Invalid age', or 'Invalid email'.",
    input_lines=["Line 1: Name", "Line 2: Age", "Line 3: Email"],
    inputs=["Asha\n20\nasha@x.com", "Bob\n200\nb@x.com", "Sam\n25\nsamx.com",
            "\n20\na@x.com", "Meera\nabc\nm@x.com", "Zed\n0\nz@x.com",
            "Kabir\n120\nk@x.com"],
    solution="""
        name = input()
        age_text = input()
        email = input()
        try:
            if name.strip() == "":
                raise ValueError("Invalid name")
            try:
                age = int(age_text)
            except ValueError:
                raise ValueError("Invalid age")
            if not (1 <= age <= 120):
                raise ValueError("Invalid age")
            if "@" not in email:
                raise ValueError("Invalid email")
            print("Valid")
        except ValueError as e:
            print(e)
    """))

Q.append(dict(
    title="Calculator with Errors", difficulty="Hard", topics=TOPIC, subTopics=TRY,
    prose="Read a number, an operator (+, -, *, or /), and a second number. Print "
          "the result, 'Cannot divide by zero' for division by zero, or 'Unknown "
          "operator' if the operator is not one of the four.",
    input_lines=["Line 1: First number", "Line 2: Operator", "Line 3: Second number"],
    inputs=["6\n/\n0", "5\n%\n2", "10\n+\n5", "0\n*\n5", "-6\n-\n2",
            "7\n/\n2", "10\n^\n3"],
    solution="""
        a = int(input())
        op = input()
        b = int(input())
        try:
            if op == "+":
                print(a + b)
            elif op == "-":
                print(a - b)
            elif op == "*":
                print(a * b)
            elif op == "/":
                print(a // b)
            else:
                raise ValueError("Unknown operator")
        except ZeroDivisionError:
            print("Cannot divide by zero")
        except ValueError as e:
            print(e)
    """))

Q.append(dict(
    title="Parse CSV Safely", difficulty="Hard", topics=TOPIC, subTopics=VAL,
    prose="Read N lines, each meant to be 'name,age'. A line is valid only if it has "
          "exactly two fields, a non-empty name, and an age that is a whole number. "
          "Print the names from the valid lines, one per line.",
    input_lines=["Line 1: N", "Next N lines: records"],
    inputs=["3\nasha,20\nbad\nsam,x", "2\na,10\nb,20", "2\nx,5\n,7",
            "0", "1\nzed,1", "4\na,1,2\nb,2\nc\nd,x", "1\n,10"],
    solution="""
        n = int(input())
        for _ in range(n):
            line = input()
            parts = line.split(",")
            try:
                if len(parts) != 2:
                    raise ValueError()
                name, age = parts
                if name == "":
                    raise ValueError()
                int(age)
                print(name)
            except ValueError:
                continue
    """))

Q.append(dict(
    title="Password Strength", difficulty="Hard", topics=TOPIC, subTopics=RAISE,
    prose="Read a password. It must be at least 6 characters long and contain at "
          "least one digit. Print 'Strong' if both hold, 'Too short' if it is under "
          "6 characters, or 'Needs a digit' if it has no digit.",
    input_lines=["Line 1: A password"],
    inputs=["abc123", "ab1", "abcdef", "123456", "abcde1", "\n", "abc12345"],
    solution="""
        class WeakPassword(Exception):
            pass

        password = input()
        try:
            if len(password) < 6:
                raise WeakPassword("Too short")
            if not any(ch.isdigit() for ch in password):
                raise WeakPassword("Needs a digit")
            print("Strong")
        except WeakPassword as e:
            print(e)
    """))

Q.append(dict(
    title="Safe JSON Parse", difficulty="Hard", topics=TOPIC, subTopics=TRY,
    prose="Read one line and try to parse it as a JSON object. If it is not valid "
          "JSON, print 'Invalid JSON'. Otherwise print how many keys the object "
          "has.",
    input_lines=["Line 1: A possible JSON object"],
    inputs=['{"a": 1, "b": 2}', "not json", "{}", '{"single": 1}',
            "[1,2,3]", "{invalid", '{"a":1,"b":2,"c":3}'],
    solution="""
        import json
        line = input()
        try:
            data = json.loads(line)
            print(len(data))
        except json.JSONDecodeError:
            print("Invalid JSON")
    """))

Q.append(dict(
    title="Grade with Validation", difficulty="Hard", topics=TOPIC, subTopics=VAL,
    prose="Read a mark. If it is not between 0 and 100, print 'Invalid marks'. "
          "Otherwise print the grade: 'A' for 90 or more, 'B' for 75 or more, 'C' "
          "for 60 or more, and 'F' below that.",
    input_lines=["Line 1: A mark"],
    inputs=["95", "150", "72", "0", "100", "-5", "59"],
    solution="""
        marks = int(input())
        try:
            if not (0 <= marks <= 100):
                raise ValueError()
            if marks >= 90:
                print("A")
            elif marks >= 75:
                print("B")
            elif marks >= 60:
                print("C")
            else:
                print("F")
        except ValueError:
            print("Invalid marks")
    """))

Q.append(dict(
    title="Batch Convert", difficulty="Hard", topics=TOPIC, subTopics=TRY,
    prose="Read N values on separate lines and try to convert each to a whole "
          "number. Print 'ok X fail Y' with the counts of successful and failed "
          "conversions.",
    input_lines=["Line 1: N", "Next N lines: values"],
    inputs=["4\n1\n2\nx\n3", "2\na\nb", "1\n5", "0", "1\n0",
            "3\n-1\n-2\n-3", "5\n1\n2\n3\n4\n5"],
    solution="""
        n = int(input())
        ok = fail = 0
        for _ in range(n):
            try:
                int(input())
                ok += 1
            except ValueError:
                fail += 1
        print(f"ok {ok} fail {fail}")
    """))

Q.append(dict(
    title="Safe Matrix Access", difficulty="Hard", topics=TOPIC, subTopics=TRY,
    prose="Read a grid with R rows and C columns, then Q queries, each a row and "
          "column. For each query print the value at that position, or 'Out of "
          "bounds' if the position is outside the grid.",
    input_lines=["Line 1: R and C", "Next R lines: grid rows", "Then: Q",
                 "Next Q lines: 'row col'"],
    inputs=["2 2\n1 2\n3 4\n2\n0 1\n5 5", "1 1\n9\n1\n0 0",
            "2 2\n1 2\n3 4\n1\n1 1", "1 1\n5\n1\n-1 0", "1 1\n5\n0",
            "3 3\n1 2 3\n4 5 6\n7 8 9\n2\n2 2\n0 0", "2 2\n1 2\n3 4\n1\n10 10"],
    solution="""
        r, c = map(int, input().split())
        grid = [list(map(int, input().split())) for _ in range(r)]
        q = int(input())
        for _ in range(q):
            row, col = map(int, input().split())
            try:
                if row < 0 or col < 0:
                    raise IndexError()
                print(grid[row][col])
            except IndexError:
                print("Out of bounds")
    """))

Q.append(dict(
    title="Robust Statistics", difficulty="Hard", topics=TOPIC, subTopics=TRY,
    prose="Read a line of tokens. Compute the average of the ones that are valid "
          "numbers, printed to 1 decimal place. If none of the tokens are valid "
          "numbers, print 'No valid data'.",
    input_lines=["Line 1: Space-separated tokens"],
    inputs=["10 20 x 30", "a b c", "5 5", "0 0", "-5 5 -10", "1 2 3 4 5",
            "x y 10"],
    solution="""
        numbers = []
        for token in input().split():
            try:
                numbers.append(int(token))
            except ValueError:
                pass
        try:
            print(round(sum(numbers) / len(numbers), 1))
        except ZeroDivisionError:
            print("No valid data")
    """))

if __name__ == "__main__":
    out = os.path.abspath(os.path.join(
        os.path.dirname(__file__), "..",
        "Unit 12 - Exception Handling",
        "Unit 12 - Exception Handling - Coding Questions.xlsx"))
    os.makedirs(os.path.dirname(out), exist_ok=True)
    main(Q, out)
