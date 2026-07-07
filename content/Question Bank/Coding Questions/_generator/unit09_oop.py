"""Unit 9 - Basic Object-Oriented Programming - Coding Questions (30: 10/10/10).

Scope: classes & objects, instantiation, attributes, methods & self,
the __init__ constructor. Single-inheritance/advanced OOP is out of scope.
"""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from cqlib import main

TOPIC = "oop"
CLS, ATTR, INIT = "classes-objects", "attributes-methods", "constructors"

Q = []

# ----------------------------- EASY (10) -----------------------------
Q.append(dict(
    title="Rectangle Area Class", difficulty="Easy", topics=TOPIC, subTopics=CLS,
    prose="Define a Rectangle class with a width and a height and a method that "
          "returns its area. Read a width and height, create a Rectangle, and print "
          "its area.",
    input_lines=["Line 1: Width", "Line 2: Height"],
    inputs=["3\n4", "5\n5", "2\n10", "1\n1", "0\n5", "7\n3", "100\n100"],
    solution="""
        class Rectangle:
            def __init__(self, width, height):
                self.width = width
                self.height = height

            def area(self):
                return self.width * self.height

        w = int(input())
        h = int(input())
        print(Rectangle(w, h).area())
    """))

Q.append(dict(
    title="Circle Area Class", difficulty="Easy", topics=TOPIC, subTopics=CLS,
    prose="Define a Circle class with a radius and a method that returns its area "
          "(use 3.14 for pi). Read a radius and print the area rounded to 2 decimal "
          "places.",
    input_lines=["Line 1: Radius"],
    inputs=["1", "2", "5", "0", "10", "3", "100"],
    solution="""
        class Circle:
            def __init__(self, radius):
                self.radius = radius

            def area(self):
                return 3.14 * self.radius * self.radius

        r = int(input())
        print(round(Circle(r).area(), 2))
    """))

Q.append(dict(
    title="Student Greeting", difficulty="Easy", topics=TOPIC, subTopics=ATTR,
    prose="Define a Student class that stores a name and has a method greet() "
          "returning 'Hi, I am <name>'. Read a name and print the greeting.",
    input_lines=["Line 1: A name"],
    inputs=["Asha", "Kabir", "Sam", "A", "Priya", "Z", "Mohammed"],
    solution="""
        class Student:
            def __init__(self, name):
                self.name = name

            def greet(self):
                return f"Hi, I am {self.name}"

        print(Student(input()).greet())
    """))

Q.append(dict(
    title="Click Counter", difficulty="Easy", topics=TOPIC, subTopics=ATTR,
    prose="Define a Counter class that starts at 0 and has an increment() method. "
          "Read N, increment a Counter N times, and print its final count.",
    input_lines=["Line 1: N, the number of clicks"],
    inputs=["5", "0", "3", "1", "10", "2", "100"],
    solution="""
        class Counter:
            def __init__(self):
                self.count = 0

            def increment(self):
                self.count += 1

        n = int(input())
        c = Counter()
        for _ in range(n):
            c.increment()
        print(c.count)
    """))

Q.append(dict(
    title="Simple Deposit", difficulty="Easy", topics=TOPIC, subTopics=ATTR,
    prose="Define a BankAccount class with a balance and a deposit(amount) method. "
          "Read a starting balance and a deposit amount, apply the deposit, and "
          "print the new balance.",
    input_lines=["Line 1: Starting balance", "Line 2: Deposit amount"],
    inputs=["100\n50", "0\n200", "500\n0", "0\n0", "1\n1", "-50\n100", "1000\n2000"],
    solution="""
        class BankAccount:
            def __init__(self, balance):
                self.balance = balance

            def deposit(self, amount):
                self.balance += amount

        start = int(input())
        amount = int(input())
        account = BankAccount(start)
        account.deposit(amount)
        print(account.balance)
    """))

Q.append(dict(
    title="Dog Bark", difficulty="Easy", topics=TOPIC, subTopics=CLS,
    prose="Define a Dog class that stores a name and has a bark() method returning "
          "'<name> says Woof'. Read a name and print the bark.",
    input_lines=["Line 1: The dog's name"],
    inputs=["Rex", "Bruno", "Milo", "A", "Fido", "Z", "Buddy"],
    solution="""
        class Dog:
            def __init__(self, name):
                self.name = name

            def bark(self):
                return f"{self.name} says Woof"

        print(Dog(input()).bark())
    """))

Q.append(dict(
    title="Point Printer", difficulty="Easy", topics=TOPIC, subTopics=INIT,
    prose="Define a Point class that stores x and y coordinates. Read x and y, "
          "create a Point, and print it in the form (x, y).",
    input_lines=["Line 1: x", "Line 2: y"],
    inputs=["3\n4", "0\n0", "-1\n5", "1\n1", "-5\n-5", "100\n-100", "0\n1"],
    solution="""
        class Point:
            def __init__(self, x, y):
                self.x = x
                self.y = y

        x = int(input())
        y = int(input())
        p = Point(x, y)
        print(f"({p.x}, {p.y})")
    """))

Q.append(dict(
    title="Book Info", difficulty="Easy", topics=TOPIC, subTopics=ATTR,
    prose="Define a Book class that stores a title and an author and has a method "
          "describe() returning '<title> by <author>'. Read a title and an author "
          "and print the description.",
    input_lines=["Line 1: Title", "Line 2: Author"],
    inputs=["Python\nGuido", "Domain Design\nEvans", "X\nY", "A\nB", "1984\nOrwell",
            "War and Peace\nTolstoy", "C\nD"],
    solution="""
        class Book:
            def __init__(self, title, author):
                self.title = title
                self.author = author

            def describe(self):
                return f"{self.title} by {self.author}"

        title = input()
        author = input()
        print(Book(title, author).describe())
    """))

Q.append(dict(
    title="Thermometer Object", difficulty="Easy", topics=TOPIC, subTopics=ATTR,
    prose="Define a Thermometer class that stores a Celsius temperature and has a "
          "method to_fahrenheit() using F = C * 9 / 5 + 32. Read a Celsius value "
          "and print the Fahrenheit value rounded to 1 decimal place.",
    input_lines=["Line 1: Temperature in Celsius"],
    inputs=["0", "100", "37", "-40", "-273.15", "98.6", "1000"],
    solution="""
        class Thermometer:
            def __init__(self, celsius):
                self.celsius = celsius

            def to_fahrenheit(self):
                return self.celsius * 9 / 5 + 32

        t = Thermometer(float(input()))
        print(round(t.to_fahrenheit(), 1))
    """))

Q.append(dict(
    title="Car Description", difficulty="Easy", topics=TOPIC, subTopics=INIT,
    prose="Define a Car class that stores a brand and a year and has a method "
          "describe() returning '<year> <brand>'. Read a brand and a year and "
          "print the description.",
    input_lines=["Line 1: Brand", "Line 2: Year"],
    inputs=["Toyota\n2020", "Honda\n2018", "BMW\n2023", "Kia\n1999", "Tesla\n2024",
            "Ford\n2000", "Audi\n2015"],
    solution="""
        class Car:
            def __init__(self, brand, year):
                self.brand = brand
                self.year = year

            def describe(self):
                return f"{self.year} {self.brand}"

        brand = input()
        year = input()
        print(Car(brand, year).describe())
    """))

# ----------------------------- MEDIUM (10) -----------------------------
Q.append(dict(
    title="Deposit and Withdraw", difficulty="Medium", topics=TOPIC, subTopics=ATTR,
    prose="Define a BankAccount class with deposit and withdraw methods; a withdraw "
          "that exceeds the balance is ignored. Read a starting balance, then N "
          "operations like 'deposit 50' or 'withdraw 30', and print the final "
          "balance.",
    input_lines=["Line 1: Starting balance", "Line 2: N",
                 "Next N lines: 'deposit X' or 'withdraw X'"],
    inputs=["100\n3\ndeposit 50\nwithdraw 30\nwithdraw 500",
            "0\n1\ndeposit 100", "50\n2\nwithdraw 20\nwithdraw 40",
            "0\n0", "10\n1\nwithdraw 10", "0\n2\ndeposit 5\nwithdraw 5",
            "1000\n4\ndeposit 100\nwithdraw 50\ndeposit 200\nwithdraw 1000"],
    solution="""
        class BankAccount:
            def __init__(self, balance):
                self.balance = balance

            def deposit(self, amount):
                self.balance += amount

            def withdraw(self, amount):
                if amount <= self.balance:
                    self.balance -= amount

        account = BankAccount(int(input()))
        n = int(input())
        for _ in range(n):
            op, amount = input().split()
            amount = int(amount)
            if op == "deposit":
                account.deposit(amount)
            else:
                account.withdraw(amount)
        print(account.balance)
    """))

Q.append(dict(
    title="Rectangle Area and Perimeter", difficulty="Medium", topics=TOPIC, subTopics=ATTR,
    prose="Define a Rectangle class with methods area() and perimeter(). Read a "
          "width and height and print the area and perimeter separated by a space.",
    input_lines=["Line 1: Width", "Line 2: Height"],
    inputs=["3\n4", "5\n5", "2\n10", "1\n1", "0\n5", "7\n3", "100\n100"],
    solution="""
        class Rectangle:
            def __init__(self, width, height):
                self.width = width
                self.height = height

            def area(self):
                return self.width * self.height

            def perimeter(self):
                return 2 * (self.width + self.height)

        w = int(input())
        h = int(input())
        r = Rectangle(w, h)
        print(r.area(), r.perimeter())
    """))

Q.append(dict(
    title="Student Average", difficulty="Medium", topics=TOPIC, subTopics=ATTR,
    prose="Define a Student class that stores a name and a list of marks and has an "
          "average() method. Read a name, then a line of marks, and print '<name> "
          "<average>' with the average rounded to 2 decimal places.",
    input_lines=["Line 1: Name", "Line 2: Space-separated marks"],
    inputs=["Asha\n80 90 100", "Sam\n50", "Bob\n60 70", "Zoe\n0", "Ann\n100 100 100",
            "Ray\n1 2 3 4 5", "Kim\n0 0 100"],
    solution="""
        class Student:
            def __init__(self, name, marks):
                self.name = name
                self.marks = marks

            def average(self):
                return sum(self.marks) / len(self.marks)

        name = input()
        marks = list(map(int, input().split()))
        s = Student(name, marks)
        print(name, round(s.average(), 2))
    """))

Q.append(dict(
    title="Stack Class", difficulty="Medium", topics=TOPIC, subTopics=ATTR,
    prose="Define a Stack class with push and pop methods backed by a list. Read N "
          "operations ('push X' or 'pop'), then print the remaining items from "
          "bottom to top separated by spaces, or 'empty' if the stack is empty.",
    input_lines=["Line 1: N", "Next N lines: 'push X' or 'pop'"],
    inputs=["4\npush 1\npush 2\npop\npush 3", "2\npush 5\npop",
            "3\npush 7\npush 8\npush 9", "0", "1\npop", "2\npop\npop",
            "6\npush 1\npush 2\npush 3\npop\npop\npop"],
    solution="""
        class Stack:
            def __init__(self):
                self.items = []

            def push(self, value):
                self.items.append(value)

            def pop(self):
                if self.items:
                    self.items.pop()

        stack = Stack()
        n = int(input())
        for _ in range(n):
            parts = input().split()
            if parts[0] == "push":
                stack.push(parts[1])
            else:
                stack.pop()
        print(" ".join(stack.items) if stack.items else "empty")
    """))

Q.append(dict(
    title="Running Maximum", difficulty="Medium", topics=TOPIC, subTopics=ATTR,
    prose="Define a class that tracks the largest number it has seen through an "
          "add(value) method. Read a line of numbers, add each one, and print the "
          "largest.",
    input_lines=["Line 1: Space-separated numbers"],
    inputs=["3 1 4 1 5", "7", "-1 -2", "0", "-5 -3 -8", "1 2 3 4 5 6 7 8 9", "100 -100"],
    solution="""
        class MaxTracker:
            def __init__(self):
                self.best = None

            def add(self, value):
                if self.best is None or value > self.best:
                    self.best = value

        tracker = MaxTracker()
        for x in map(int, input().split()):
            tracker.add(x)
        print(tracker.best)
    """))

Q.append(dict(
    title="Circle Area and Circumference", difficulty="Medium", topics=TOPIC, subTopics=ATTR,
    prose="Define a Circle class with methods area() and circumference() (use 3.14 "
          "for pi). Read a radius and print the area and circumference, each "
          "rounded to 2 decimal places, separated by a space.",
    input_lines=["Line 1: Radius"],
    inputs=["1", "2", "5", "0", "10", "3", "100"],
    solution="""
        class Circle:
            def __init__(self, radius):
                self.radius = radius

            def area(self):
                return 3.14 * self.radius * self.radius

            def circumference(self):
                return 2 * 3.14 * self.radius

        c = Circle(int(input()))
        print(round(c.area(), 2), round(c.circumference(), 2))
    """))

Q.append(dict(
    title="Give a Raise", difficulty="Medium", topics=TOPIC, subTopics=ATTR,
    prose="Define an Employee class with a salary and a give_raise(percent) method "
          "that increases the salary by that percentage. Read a salary and a "
          "percentage, apply the raise, and print the new salary rounded to 2 "
          "decimal places.",
    input_lines=["Line 1: Salary", "Line 2: Raise percentage"],
    inputs=["1000\n10", "5000\n0", "2000\n50", "0\n10", "1000\n100", "1\n1", "10000\n25"],
    solution="""
        class Employee:
            def __init__(self, salary):
                self.salary = salary

            def give_raise(self, percent):
                self.salary += self.salary * percent / 100

        salary = int(input())
        percent = int(input())
        e = Employee(salary)
        e.give_raise(percent)
        print(round(e.salary, 2))
    """))

Q.append(dict(
    title="Bigger Rectangle", difficulty="Medium", topics=TOPIC, subTopics=ATTR,
    prose="Define a Rectangle class with an area() method. Read two rectangles (each "
          "as a width and height on one line) and print 'First' if the first has "
          "the larger area, 'Second' if the second does, or 'Equal' if they match.",
    input_lines=["Line 1: width1 height1", "Line 2: width2 height2"],
    inputs=["3 4\n5 5", "6 2\n3 4", "10 10\n2 2", "1 1\n1 1", "0 5\n5 0",
            "100 1\n1 100", "5 5\n5 5"],
    solution="""
        class Rectangle:
            def __init__(self, width, height):
                self.width = width
                self.height = height

            def area(self):
                return self.width * self.height

        w1, h1 = map(int, input().split())
        w2, h2 = map(int, input().split())
        a1 = Rectangle(w1, h1).area()
        a2 = Rectangle(w2, h2).area()
        if a1 > a2:
            print("First")
        elif a2 > a1:
            print("Second")
        else:
            print("Equal")
    """))

Q.append(dict(
    title="Shopping Cart Total", difficulty="Medium", topics=TOPIC, subTopics=ATTR,
    prose="Define a Cart class with an add(price, quantity) method and a total() "
          "method. Read N items, each with a name, price, and quantity, add them, "
          "and print the cart total.",
    input_lines=["Line 1: N", "Next N lines: 'name price quantity'"],
    inputs=["2\napple 10 3\nbread 20 2", "1\nmilk 15 1", "2\na 5 5\nb 1 10",
            "0", "1\nfree 0 5", "1\nx 100 1", "3\na 1 1\nb 2 2\nc 3 3"],
    solution="""
        class Cart:
            def __init__(self):
                self.amount = 0

            def add(self, price, quantity):
                self.amount += price * quantity

            def total(self):
                return self.amount

        cart = Cart()
        n = int(input())
        for _ in range(n):
            name, price, quantity = input().split()
            cart.add(int(price), int(quantity))
        print(cart.total())
    """))

Q.append(dict(
    title="BMI Calculator", difficulty="Medium", topics=TOPIC, subTopics=ATTR,
    prose="Define a Person class that stores weight (kg) and height (m) and has a "
          "bmi() method returning weight / (height * height). Read a weight and a "
          "height and print the BMI rounded to 1 decimal place.",
    input_lines=["Line 1: Weight in kg", "Line 2: Height in m"],
    inputs=["70\n1.75", "60\n1.6", "80\n2.0", "50\n1.5", "100\n2.0", "45\n1.4", "90\n1.8"],
    solution="""
        class Person:
            def __init__(self, weight, height):
                self.weight = weight
                self.height = height

            def bmi(self):
                return self.weight / (self.height * self.height)

        weight = float(input())
        height = float(input())
        print(round(Person(weight, height).bmi(), 1))
    """))

# ----------------------------- HARD (10) -----------------------------
Q.append(dict(
    title="Bank Statement", difficulty="Hard", topics=TOPIC, subTopics=ATTR,
    prose="Define a BankAccount class where withdraw returns whether it succeeded. "
          "Read a starting balance and N operations ('deposit X' or 'withdraw X'). "
          "After each operation print the new balance, or 'Denied' if a withdrawal "
          "was refused for insufficient funds.",
    input_lines=["Line 1: Starting balance", "Line 2: N",
                 "Next N lines: 'deposit X' or 'withdraw X'"],
    inputs=["100\n3\ndeposit 50\nwithdraw 200\nwithdraw 100",
            "0\n2\ndeposit 100\nwithdraw 40", "50\n1\nwithdraw 60",
            "0\n0", "10\n1\nwithdraw 10", "0\n1\nwithdraw 1",
            "1000\n4\ndeposit 500\nwithdraw 2000\nwithdraw 500\ndeposit 100"],
    solution="""
        class BankAccount:
            def __init__(self, balance):
                self.balance = balance

            def deposit(self, amount):
                self.balance += amount
                return True

            def withdraw(self, amount):
                if amount > self.balance:
                    return False
                self.balance -= amount
                return True

        account = BankAccount(int(input()))
        n = int(input())
        for _ in range(n):
            op, amount = input().split()
            amount = int(amount)
            if op == "deposit":
                account.deposit(amount)
                print(account.balance)
            else:
                if account.withdraw(amount):
                    print(account.balance)
                else:
                    print("Denied")
    """))

Q.append(dict(
    title="Class Topper", difficulty="Hard", topics=TOPIC, subTopics=ATTR,
    prose="Define a Student class that stores a name and marks and can report its "
          "total. Read N students, each with a name followed by three marks, and "
          "print the name and total of the top scorer (earliest one on a tie).",
    input_lines=["Line 1: N", "Next N lines: 'name m1 m2 m3'"],
    inputs=["3\nasha 80 90 100\nkabir 70 60 50\nmeera 90 90 90",
            "1\nsam 50 50 50", "2\na 10 10 10\nb 20 20 20",
            "2\nx 0 0 0\ny 0 0 0", "1\nsolo 100 100 100",
            "4\na 1 1 1\nb 2 2 2\nc 3 3 3\nd 4 4 4", "3\np 50 50 50\nq 50 50 50\nr 50 50 50"],
    solution="""
        class Student:
            def __init__(self, name, marks):
                self.name = name
                self.marks = marks

            def total(self):
                return sum(self.marks)

        n = int(input())
        best = None
        for _ in range(n):
            parts = input().split()
            student = Student(parts[0], [int(m) for m in parts[1:]])
            if best is None or student.total() > best.total():
                best = student
        print(best.name, best.total())
    """))

Q.append(dict(
    title="Fraction Addition", difficulty="Hard", topics=TOPIC, subTopics=ATTR,
    prose="Define a Fraction class with a method that adds another fraction and "
          "returns the result in lowest terms. Read two fractions written as "
          "'a/b', add them, and print the reduced result as 'p/q'.",
    input_lines=["Line 1: First fraction 'a/b'", "Line 2: Second fraction 'a/b'"],
    inputs=["1/2\n1/3", "1/4\n1/4", "2/3\n1/3", "1/1\n1/1", "0/1\n1/2",
            "1/6\n1/3", "5/8\n3/8"],
    solution="""
        import math

        class Fraction:
            def __init__(self, num, den):
                self.num = num
                self.den = den

            def add(self, other):
                num = self.num * other.den + other.num * self.den
                den = self.den * other.den
                g = math.gcd(num, den)
                return Fraction(num // g, den // g)

        a = input().split("/")
        b = input().split("/")
        f1 = Fraction(int(a[0]), int(a[1]))
        f2 = Fraction(int(b[0]), int(b[1]))
        result = f1.add(f2)
        print(f"{result.num}/{result.den}")
    """))

Q.append(dict(
    title="Vector Operations", difficulty="Hard", topics=TOPIC, subTopics=ATTR,
    prose="Define a Vector class with methods to add another vector and to compute "
          "the dot product. Read two vectors of equal length (space-separated), "
          "print their sum on one line and their dot product on the next.",
    input_lines=["Line 1: First vector", "Line 2: Second vector"],
    inputs=["1 2 3\n4 5 6", "1 0\n0 1", "2 2\n3 3", "0 0\n0 0", "-1 -2\n1 2",
            "5\n5", "1 2 3 4 5\n5 4 3 2 1"],
    solution="""
        class Vector:
            def __init__(self, values):
                self.values = values

            def add(self, other):
                return Vector([a + b for a, b in zip(self.values, other.values)])

            def dot(self, other):
                return sum(a * b for a, b in zip(self.values, other.values))

        v1 = Vector(list(map(int, input().split())))
        v2 = Vector(list(map(int, input().split())))
        print(*v1.add(v2).values)
        print(v1.dot(v2))
    """))

Q.append(dict(
    title="Inventory Manager", difficulty="Hard", topics=TOPIC, subTopics=ATTR,
    prose="Define an Inventory class that tracks item quantities with add and "
          "remove methods. Read N operations ('add item qty' or 'remove item "
          "qty'), then print each item with a positive quantity as 'item:qty', "
          "sorted by item name.",
    input_lines=["Line 1: N", "Next N lines: 'add item qty' or 'remove item qty'"],
    inputs=["4\nadd apple 5\nadd banana 3\nremove apple 2\nadd cherry 4",
            "2\nadd milk 2\nadd milk 3", "3\nadd a 5\nremove a 2\nadd b 1",
            "0", "1\nadd x 1", "2\nadd x 5\nremove x 5",
            "5\nadd a 10\nadd b 20\nremove a 10\nadd c 5\nremove b 25"],
    solution="""
        class Inventory:
            def __init__(self):
                self.items = {}

            def add(self, item, qty):
                self.items[item] = self.items.get(item, 0) + qty

            def remove(self, item, qty):
                self.items[item] = self.items.get(item, 0) - qty

        inv = Inventory()
        n = int(input())
        for _ in range(n):
            op, item, qty = input().split()
            if op == "add":
                inv.add(item, int(qty))
            else:
                inv.remove(item, int(qty))
        for item in sorted(inv.items):
            if inv.items[item] > 0:
                print(f"{item}:{inv.items[item]}")
    """))

Q.append(dict(
    title="Time Adder", difficulty="Hard", topics=TOPIC, subTopics=ATTR,
    prose="Define a Time class storing hours and minutes with a method to add "
          "another Time, carrying minutes over 60 into hours. Read two times "
          "written as 'h:m', add them, and print the result as 'h:mm' (minutes "
          "always two digits).",
    input_lines=["Line 1: First time 'h:m'", "Line 2: Second time 'h:m'"],
    inputs=["1:30\n2:45", "0:50\n0:20", "2:00\n3:00", "0:0\n0:0", "23:59\n0:1",
            "5:45\n5:45", "12:30\n1:45"],
    solution="""
        class Time:
            def __init__(self, hours, minutes):
                self.hours = hours
                self.minutes = minutes

            def add(self, other):
                total = self.minutes + other.minutes
                carry = total // 60
                minutes = total % 60
                hours = self.hours + other.hours + carry
                return Time(hours, minutes)

        a = input().split(":")
        b = input().split(":")
        t1 = Time(int(a[0]), int(a[1]))
        t2 = Time(int(b[0]), int(b[1]))
        result = t1.add(t2)
        print(f"{result.hours}:{result.minutes:02d}")
    """))

Q.append(dict(
    title="Count Instances", difficulty="Hard", topics=TOPIC, subTopics=CLS,
    prose="Define a Widget class that uses a class-level counter to track how many "
          "Widgets have been created, incremented in __init__. Read N, create N "
          "Widgets, and print how many exist.",
    input_lines=["Line 1: N"],
    inputs=["5", "1", "3", "0", "10", "2", "100"],
    solution="""
        class Widget:
            count = 0

            def __init__(self):
                Widget.count += 1

        n = int(input())
        for _ in range(n):
            Widget()
        print(Widget.count)
    """))

Q.append(dict(
    title="Payroll", difficulty="Hard", topics=TOPIC, subTopics=ATTR,
    prose="Define an Employee class with a pay() method: hours up to 40 are paid at "
          "the normal rate, and any hours beyond 40 are paid at 1.5 times the rate. "
          "Read N employees, each with a name, hours, and hourly rate, and print "
          "'name pay' for each.",
    input_lines=["Line 1: N", "Next N lines: 'name hours rate'"],
    inputs=["2\nasha 45 10\nkabir 40 20", "1\nsam 20 10", "2\na 50 10\nb 30 10",
            "1\nzero 0 10", "1\nexact 40 15", "1\nmax 60 20",
            "3\na 10 10\nb 40 10\nc 41 10"],
    solution="""
        class Employee:
            def __init__(self, name, hours, rate):
                self.name = name
                self.hours = hours
                self.rate = rate

            def pay(self):
                if self.hours <= 40:
                    return self.hours * self.rate
                return 40 * self.rate + (self.hours - 40) * self.rate * 1.5

        n = int(input())
        for _ in range(n):
            name, hours, rate = input().split()
            e = Employee(name, int(hours), int(rate))
            pay = e.pay()
            print(name, int(pay) if pay == int(pay) else pay)
    """))

Q.append(dict(
    title="Polynomial Evaluation", difficulty="Hard", topics=TOPIC, subTopics=ATTR,
    prose="Define a Polynomial class that stores coefficients from the highest power "
          "down to the constant and has an evaluate(x) method. Read the "
          "coefficients on one line and a value x, then print the polynomial "
          "evaluated at x.",
    input_lines=["Line 1: Space-separated coefficients (high power first)",
                 "Line 2: The value x"],
    inputs=["1 2 3\n2", "2 0 1\n3", "5\n10", "0\n5", "1 0 0\n0", "1 -2 1\n1",
            "3 2 1 0\n-2"],
    solution="""
        class Polynomial:
            def __init__(self, coeffs):
                self.coeffs = coeffs

            def evaluate(self, x):
                result = 0
                for c in self.coeffs:
                    result = result * x + c
                return result

        coeffs = list(map(int, input().split()))
        x = int(input())
        print(Polynomial(coeffs).evaluate(x))
    """))

Q.append(dict(
    title="Matrix Addition", difficulty="Hard", topics=TOPIC, subTopics=ATTR,
    prose="Define a Matrix class with a method to add another matrix of the same "
          "size. Read the size R and C, then two matrices, and print their sum row "
          "by row.",
    input_lines=["Line 1: R and C separated by a space",
                 "Next R lines: first matrix rows",
                 "Next R lines: second matrix rows"],
    inputs=["2 2\n1 2\n3 4\n5 6\n7 8", "1 1\n5\n7", "2 3\n1 1 1\n2 2 2\n3 3 3\n4 4 4",
            "1 2\n0 0\n0 0", "3 1\n1\n2\n3\n4\n5\n6", "2 2\n-1 -2\n-3 -4\n1 2\n3 4",
            "1 3\n1 2 3\n4 5 6"],
    solution="""
        class Matrix:
            def __init__(self, rows):
                self.rows = rows

            def add(self, other):
                return Matrix([
                    [a + b for a, b in zip(r1, r2)]
                    for r1, r2 in zip(self.rows, other.rows)
                ])

        r, c = map(int, input().split())
        m1 = [list(map(int, input().split())) for _ in range(r)]
        m2 = [list(map(int, input().split())) for _ in range(r)]
        for row in Matrix(m1).add(Matrix(m2)).rows:
            print(*row)
    """))

if __name__ == "__main__":
    out = os.path.abspath(os.path.join(
        os.path.dirname(__file__), "..",
        "Unit 9 - Basic Object-Oriented Programming",
        "Unit 9 - Basic Object-Oriented Programming - Coding Questions.xlsx"))
    os.makedirs(os.path.dirname(out), exist_ok=True)
    main(Q, out)
