## Introduction

Walk up to any shop counter and numbers are everywhere, but they are not all the same kind. You buy 3 packets of biscuits, never 3.5 of them, so a quantity is a whole number. The price, though, might be 12.50 rupees, which needs a decimal point. And in an engineering lab you may meet numbers that a school calculator cannot show.

Python gives you three built in number types for these situations: **int** for whole numbers, **float** for numbers with a decimal point, and **complex** for advanced mathematics. Each one is built differently under the hood, which is exactly why mixing them up causes trouble. A count of biscuit packets can never sensibly be 3.5, so forcing it into a decimal type would let your program accept nonsense it should refuse. A price, on the other hand, genuinely needs that decimal point, so squeezing it into a whole number would silently throw away real money. Knowing which is which saves you from a whole class of confusing bugs.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/44t82usgz/02_int_vs_float_scale.png)


## Whole Numbers: int

An integer, written `int`, is a number with no fractional part: positive, negative, or zero.

```python
apples = 3
floor = -2
students = 240
print(students)
```

Integers are perfect for counting and for anything that comes in whole units: people, items, attempts, pages. Think back to the shop counter from the introduction. The cashier never rings up "3.5 packets" of biscuits, because a packet either sits on the counter or it does not; there is no in-between state for a count to occupy. That is the real-world idea an `int` is built to capture exactly. A pleasant surprise in Python is that integers can grow as large as your memory allows, so you can multiply huge numbers without them overflowing, something many other languages cannot do as easily. A calculator might give up once the digits get long enough, but Python keeps counting.

## Numbers with a Decimal Point: float

A floating point number, written `float`, carries a decimal point and is used for measurements, money, averages, and anything that can be a fraction.

```python
price = 12.50
average = 76.4
pi = 3.14159
print(pi)
```

Now here is a question that surprises almost every beginner. What do you think this prints?

```python
print(0.1 + 0.2)
```

You would expect 0.3, but Python prints `0.30000000000000004`. This is not a bug in Python. Computers store decimals in binary, and a few values like 0.1 cannot be written exactly, just as one third cannot be written exactly as a decimal. Try writing 1/3 in base ten and you will fill the page with threes and still not finish; binary has its own set of "unfinishable" fractions, and 0.1 happens to be one of them. The tiny error is normal in every programming language, not a weakness specific to Python, and it is far too small to matter for almost anything you will calculate as a beginner. For now, simply know that it happens, and that when displaying money you will later round the result.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/44t82usgz/02_float_rounding_surprise.png)


## Complex Numbers: complex

The third type, `complex`, is for numbers with an imaginary part, written with a `j`, and it appears mostly in engineering, physics, and signal processing.

```python
z = 3 + 4j
print(z.real)   # 3.0
print(z.imag)   # 4.0
```

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/44t82usgz/02_complex_number_signal_parts.png)


If you have not met complex numbers in mathematics yet, you can safely set this type aside. It is enough to know Python supports it when you need it.

## Three Number Types at a Glance

| Type | Used For | Example | Notable Trait |
|---|---|---|---|
| `int` | Counting whole units | `students = 240` | Can grow arbitrarily large with no overflow |
| `float` | Measurements, money, decimals | `price = 12.50` | Tiny rounding errors are normal, since decimals are stored in binary |
| `complex` | Imaginary-number mathematics | `z = 3 + 4j` | Rare outside engineering, physics, and signal processing |

## Your Turn: A Two-Number Calculator

This small program reads two numbers and shows their results. Notice that we convert the typed text into numbers first, a step you will study properly in the next lesson.

```python
a = int(input("First whole number: "))
b = int(input("Second whole number: "))

print("Sum:", a + b)
print("Average:", (a + b) / 2)
```

Type 7 and 10. The sum prints as 17, a whole number, while the average prints as 8.5, a float, because dividing produced a fraction. Python chose a sensible kind of number for each result on its own.

## Conclusion

Use `int` for whole numbers you count, `float` for values that can have a decimal point, and `complex` for the rare case of imaginary numbers. Expect tiny rounding surprises with floats, because that is how all computers store decimals. Picking the type that matches the real quantity, a count versus a measurement, keeps your programs honest and your results predictable. It is a small decision that you will make almost without thinking once it becomes habit, yet it quietly prevents an entire category of bugs before they ever have a chance to appear.
