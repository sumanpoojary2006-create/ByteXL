"""Unit 7 - Sets and Dictionaries - Coding Questions (30: 10/10/10).

Scope: set uniqueness & operations, dictionary CRUD, iterating dicts,
dict comprehensions, nested dictionaries, choosing the right structure.
"""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from cqlib import main

TOPIC = "sets-and-dictionaries"
SET, DICT, COMP = "set-operations", "dictionary-operations", "dictionary-comprehensions"

Q = []

# ----------------------------- EASY (10) -----------------------------
Q.append(dict(
    title="Distinct Count", difficulty="Easy", topics=TOPIC, subTopics=SET,
    prose="Read a line of space-separated numbers and print how many distinct "
          "values there are.",
    input_lines=["Line 1: Space-separated numbers"],
    inputs=["1 2 2 3 3 3", "5 5 5", "1 2 3", "0", "1 1 1 1 1", "1 2 3 4 5 6 7 8 9 10", "9 9 8 8 7 7 6 6"],
    solution="""
        nums = input().split()
        print(len(set(nums)))
    """))

Q.append(dict(
    title="Sorted Unique", difficulty="Easy", topics=TOPIC, subTopics=SET,
    prose="Read a line of space-separated numbers and print each distinct value "
          "once, sorted from smallest to largest, separated by spaces.",
    input_lines=["Line 1: Space-separated numbers"],
    inputs=["3 1 2 3 1", "5", "4 4 4 2 2", "0", "-1 -2 -1 -2", "7 7 7 7", "1 2 3 4 5 6 7 8 9 10"],
    solution="""
        nums = list(map(int, input().split()))
        print(*sorted(set(nums)))
    """))

Q.append(dict(
    title="In Both Lists", difficulty="Easy", topics=TOPIC, subTopics=SET,
    prose="Read two lines of space-separated numbers and print the values that "
          "appear in both, sorted, separated by spaces.",
    input_lines=["Line 1: First list", "Line 2: Second list"],
    inputs=["1 2 3 4\n3 4 5 6", "1 2 3\n2 3 4", "5 6 7\n6 7 8", "0\n0", "1 2 3\n4 5 6", "-1 -2\n-2 -3", "1 2 3 4 5 6 7 8\n5 6 7 8 9 10"],
    solution="""
        a = set(map(int, input().split()))
        b = set(map(int, input().split()))
        print(*sorted(a & b))
    """))

Q.append(dict(
    title="In Either List", difficulty="Easy", topics=TOPIC, subTopics=SET,
    prose="Read two lines of space-separated numbers and print all values that "
          "appear in either list, each once, sorted, separated by spaces.",
    input_lines=["Line 1: First list", "Line 2: Second list"],
    inputs=["1 2\n2 3", "5\n6", "1 1\n2 2", "0\n0", "1 2 3\n4 5 6", "-1 -2\n-2 -3", "1 2 3 4 5\n5 6 7 8 9"],
    solution="""
        a = set(map(int, input().split()))
        b = set(map(int, input().split()))
        print(*sorted(a | b))
    """))

Q.append(dict(
    title="Only in the First", difficulty="Easy", topics=TOPIC, subTopics=SET,
    prose="Read two lines of space-separated numbers and print the values that are "
          "in the first list but not the second, sorted, separated by spaces.",
    input_lines=["Line 1: First list", "Line 2: Second list"],
    inputs=["1 2 3\n2 4", "5 6 7\n6", "1 2 3\n4 5 6", "0\n0", "1 2 3\n1 2 3", "-1 -2 -3\n-2", "1 2 3 4 5 6 7 8\n2 4 6 8"],
    solution="""
        a = set(map(int, input().split()))
        b = set(map(int, input().split()))
        print(*sorted(a - b))
    """))

Q.append(dict(
    title="Phonebook Lookup", difficulty="Easy", topics=TOPIC, subTopics=DICT,
    prose="Build a phonebook from N entries, then look up one name. Read N, then N "
          "lines each with a name and a number, then a name to look up. Print the "
          "number, or 'Not Found' if the name is not in the book.",
    input_lines=["Line 1: N", "Next N lines: 'name number'", "Last line: name to look up"],
    inputs=["3\nasha 111\nkabir 222\nmeera 333\nkabir", "1\nsam 999\nsam",
            "2\na 1\nb 2\nz", "0\nnobody", "1\nx 555\ny",
            "4\na 1\nb 2\nc 3\nd 4\nd", "5\np 10\nq 20\nr 30\ns 40\nt 50\nz"],
    solution="""
        n = int(input())
        book = {}
        for _ in range(n):
            name, number = input().split()
            book[name] = number
        query = input()
        print(book.get(query, "Not Found"))
    """))

Q.append(dict(
    title="Key Exists", difficulty="Easy", topics=TOPIC, subTopics=DICT,
    prose="Read N key/value entries, then a key. Print 'Yes' if that key is present, "
          "otherwise print 'No'.",
    input_lines=["Line 1: N", "Next N lines: 'key value'", "Last line: key to check"],
    inputs=["2\napple 3\nbanana 5\napple", "1\nx 1\ny", "2\na 1\nb 2\nb", "0\nz", "1\nsolo 9\nsolo", "3\na 1\nb 2\nc 3\nd", "4\np 1\nq 2\nr 3\ns 4\nr"],
    solution="""
        n = int(input())
        data = {}
        for _ in range(n):
            key, value = input().split()
            data[key] = value
        query = input()
        print("Yes" if query in data else "No")
    """))

Q.append(dict(
    title="Total of Values", difficulty="Easy", topics=TOPIC, subTopics=DICT,
    prose="Read N items, each with a name and a price, and print the total of all "
          "the prices.",
    input_lines=["Line 1: N", "Next N lines: 'name price'"],
    inputs=["3\npen 10\nbook 50\nbag 200", "1\ntea 15", "2\na 5\nb 5", "0", "1\nx 0", "4\na 1\nb 2\nc 3\nd 4", "5\np 100\nq 200\nr 300\ns 400\nt 500"],
    solution="""
        n = int(input())
        prices = {}
        for _ in range(n):
            name, price = input().split()
            prices[name] = int(price)
        print(sum(prices.values()))
    """))

Q.append(dict(
    title="Unique Words", difficulty="Easy", topics=TOPIC, subTopics=SET,
    prose="Read a sentence and print how many distinct words it contains.",
    input_lines=["Line 1: A sentence"],
    inputs=["the cat the dog", "hello", "a a a a", "x", "one two three four five", "cat cat dog dog bird", "a b a b a b a b"],
    solution="""
        words = input().split()
        print(len(set(words)))
    """))

Q.append(dict(
    title="Set Membership", difficulty="Easy", topics=TOPIC, subTopics=SET,
    prose="Read a line of space-separated values, then a value. Print 'Yes' if the "
          "value is in the set of values, otherwise print 'No'.",
    input_lines=["Line 1: Space-separated values", "Line 2: The value to check"],
    inputs=["1 2 3 4\n3", "a b c\nz", "5 5 5\n5", "a\na", "1 2 3\n9", "x x x x\nx", "1 2 3 4 5 6 7 8 9 10\n10"],
    solution="""
        values = set(input().split())
        query = input()
        print("Yes" if query in values else "No")
    """))

# ----------------------------- MEDIUM (10) -----------------------------
Q.append(dict(
    title="Symmetric Difference", difficulty="Medium", topics=TOPIC, subTopics=SET,
    prose="Read two lines of space-separated numbers and print the values that are "
          "in exactly one of the two lists (not both), sorted, separated by spaces.",
    input_lines=["Line 1: First list", "Line 2: Second list"],
    inputs=["1 2 3\n2 3 4", "1 2\n3 4", "5 6 7\n6 7 8", "0\n0", "1 2 3\n1 2 3", "-1 -2\n-2 -3", "1 2 3 4 5\n4 5 6 7 8"],
    solution="""
        a = set(map(int, input().split()))
        b = set(map(int, input().split()))
        print(*sorted(a ^ b))
    """))

Q.append(dict(
    title="Word Frequency", difficulty="Medium", topics=TOPIC, subTopics=DICT,
    prose="Read a sentence and, for each distinct word in order of first "
          "appearance, print 'word:count', one per line.",
    input_lines=["Line 1: A sentence"],
    inputs=["a b a c b a", "hi hi", "x y z", "solo", "a a a a a", "one two two three three three", "p q r p q r p"],
    solution="""
        words = input().split()
        counts = {}
        for w in words:
            counts[w] = counts.get(w, 0) + 1
        for w, c in counts.items():
            print(f"{w}:{c}")
    """))

Q.append(dict(
    title="Most Common Word", difficulty="Medium", topics=TOPIC, subTopics=DICT,
    prose="Read a sentence and print the word that appears most often. If several "
          "tie, print the one that appears first.",
    input_lines=["Line 1: A sentence"],
    inputs=["a b a c a", "dog cat dog cat", "one", "solo", "x x y y y", "a b c a b c a", "cat dog cat dog bird"],
    solution="""
        words = input().split()
        counts = {}
        for w in words:
            counts[w] = counts.get(w, 0) + 1
        best = max(counts.values())
        for w in words:
            if counts[w] == best:
                print(w)
                break
    """))

Q.append(dict(
    title="Square Dictionary", difficulty="Medium", topics=TOPIC, subTopics=COMP,
    prose="Read a line of space-separated numbers. For each distinct number in "
          "ascending order, print 'number:square'. Build the mapping with a "
          "dictionary comprehension.",
    input_lines=["Line 1: Space-separated numbers"],
    inputs=["3 1 2", "5", "2 2 3", "0", "-1 -2 -3", "7 7 7 7", "1 2 3 4 5 6 7 8 9 10"],
    solution="""
        nums = sorted(set(map(int, input().split())))
        squares = {x: x * x for x in nums}
        for x in nums:
            print(f"{x}:{squares[x]}")
    """))

Q.append(dict(
    title="Evens and Odds", difficulty="Medium", topics=TOPIC, subTopics=DICT,
    prose="Read a line of space-separated numbers and print how many are even and "
          "how many are odd in the form 'even X odd Y'.",
    input_lines=["Line 1: Space-separated numbers"],
    inputs=["1 2 3 4 5", "2 4 6", "1 3 5", "0", "-2 -4 -1 -3", "1", "1 2 3 4 5 6 7 8 9 10"],
    solution="""
        nums = list(map(int, input().split()))
        counts = {"even": 0, "odd": 0}
        for x in nums:
            if x % 2 == 0:
                counts["even"] += 1
            else:
                counts["odd"] += 1
        print(f"even {counts['even']} odd {counts['odd']}")
    """))

Q.append(dict(
    title="Vote Winner", difficulty="Medium", topics=TOPIC, subTopics=DICT,
    prose="Read N votes, each a candidate name on its own line, and print the "
          "winner (most votes). If there is a tie, print the name that comes first "
          "alphabetically.",
    input_lines=["Line 1: N", "Next N lines: one candidate name each"],
    inputs=["5\nasha\nkabir\nasha\nmeera\nasha", "3\na\nb\nb", "2\nx\ny", "1\nsolo", "4\nz\ny\nz\ny", "6\na\nb\nc\na\nb\na", "7\nzeta\nalpha\nzeta\nalpha\nbeta\nalpha\nzeta"],
    solution="""
        n = int(input())
        counts = {}
        for _ in range(n):
            name = input()
            counts[name] = counts.get(name, 0) + 1
        best = max(counts.values())
        winners = sorted(name for name, c in counts.items() if c == best)
        print(winners[0])
    """))

Q.append(dict(
    title="Repeated Values", difficulty="Medium", topics=TOPIC, subTopics=DICT,
    prose="Read a line of space-separated numbers and print the values that appear "
          "more than once, sorted, separated by spaces.",
    input_lines=["Line 1: Space-separated numbers"],
    inputs=["1 2 2 3 3 4", "5 5 6 6", "1 1 2 2 3", "0", "1 2 3 4 5", "7 7 7 7 7", "1 2 3 4 5 6 7 8 9 10 1 2 3"],
    solution="""
        nums = list(map(int, input().split()))
        counts = {}
        for x in nums:
            counts[x] = counts.get(x, 0) + 1
        repeated = sorted(v for v, c in counts.items() if c > 1)
        print(*repeated)
    """))

Q.append(dict(
    title="First Unique Character", difficulty="Medium", topics=TOPIC, subTopics=DICT,
    prose="Read a word and print the first character that appears exactly once. If "
          "every character repeats, print 'None'.",
    input_lines=["Line 1: A word"],
    inputs=["aabbc", "aabb", "xyz", "a", "aabbccd", "zzzzz", "abababc"],
    solution="""
        word = input()
        counts = {}
        for ch in word:
            counts[ch] = counts.get(ch, 0) + 1
        answer = "None"
        for ch in word:
            if counts[ch] == 1:
                answer = ch
                break
        print(answer)
    """))

Q.append(dict(
    title="Merge Dictionaries", difficulty="Medium", topics=TOPIC, subTopics=DICT,
    prose="Read a first set of key/value pairs, then a second set. Merge them so "
          "that keys in the second set overwrite the first, and print every "
          "'key:value' with keys sorted.",
    input_lines=["Line 1: N", "Next N lines: 'key value'", "Then: M",
                 "Next M lines: 'key value'"],
    inputs=["2\na 1\nb 2\n1\nb 9", "1\nx 5\n1\ny 6", "2\np 1\nq 2\n2\np 3\nq 4", "0\n0", "1\na 1\n0", "0\n2\nx 1\ny 2", "3\na 1\nb 2\nc 3\n3\nc 9\nd 8\ne 7"],
    solution="""
        merged = {}
        n = int(input())
        for _ in range(n):
            key, value = input().split()
            merged[key] = value
        m = int(input())
        for _ in range(m):
            key, value = input().split()
            merged[key] = value
        for key in sorted(merged):
            print(f"{key}:{merged[key]}")
    """))

Q.append(dict(
    title="Spending by Category", difficulty="Medium", topics=TOPIC, subTopics=DICT,
    prose="Read N spending records, each a category and an amount. Print each "
          "category's total as 'category:total', with categories sorted "
          "alphabetically.",
    input_lines=["Line 1: N", "Next N lines: 'category amount'"],
    inputs=["3\nfood 100\ntravel 50\nfood 30", "1\nrent 500", "2\na 5\na 5", "0", "1\nz 0", "4\nfood 10\ntravel 20\nfood 30\nbills 40", "5\na 1\nb 2\na 3\nb 4\nc 5"],
    solution="""
        n = int(input())
        totals = {}
        for _ in range(n):
            category, amount = input().split()
            totals[category] = totals.get(category, 0) + int(amount)
        for category in sorted(totals):
            print(f"{category}:{totals[category]}")
    """))

# ----------------------------- HARD (10) -----------------------------
Q.append(dict(
    title="Student Totals", difficulty="Hard", topics=TOPIC, subTopics=DICT,
    prose="Read N students, each on a line with a name followed by their marks. "
          "Print each student's name and total marks as 'name total', with names "
          "sorted alphabetically.",
    input_lines=["Line 1: N", "Next N lines: 'name mark1 mark2 ...'"],
    inputs=["2\nasha 80 90 100\nkabir 70 60 50", "1\nsam 40 60",
            "3\nc 1 2\nb 3 4\na 5 6", "0", "1\nsolo 0 0 0",
            "4\nzed 10\nalpha 20\nmid 30\nbeta 40", "5\np 1 1\nq 2 2\nr 3 3\ns 4 4\nt 5 5"],
    solution="""
        n = int(input())
        totals = {}
        for _ in range(n):
            parts = input().split()
            name = parts[0]
            totals[name] = sum(int(m) for m in parts[1:])
        for name in sorted(totals):
            print(name, totals[name])
    """))

Q.append(dict(
    title="Word Count Ranking", difficulty="Hard", topics=TOPIC, subTopics=DICT,
    prose="Read a sentence and print each distinct word with its count as 'word "
          "count', ordered by count from highest to lowest. Break ties "
          "alphabetically.",
    input_lines=["Line 1: A sentence"],
    inputs=["a b a c b a", "dog cat dog", "x y z", "solo", "a a b b c c", "z y x z y z", "one two two three three three"],
    solution="""
        words = input().split()
        counts = {}
        for w in words:
            counts[w] = counts.get(w, 0) + 1
        for w, c in sorted(counts.items(), key=lambda t: (-t[1], t[0])):
            print(w, c)
    """))

Q.append(dict(
    title="Character Frequency Ranking", difficulty="Hard", topics=TOPIC, subTopics=DICT,
    prose="Read a word and print each character with its count as 'char:count', "
          "ordered by count from highest to lowest, breaking ties alphabetically.",
    input_lines=["Line 1: A word"],
    inputs=["hello", "aabbcc", "mississippi", "a", "zzzzyyyxx", "abcabcabc", "banana"],
    solution="""
        word = input()
        counts = {}
        for ch in word:
            counts[ch] = counts.get(ch, 0) + 1
        for ch, c in sorted(counts.items(), key=lambda t: (-t[1], t[0])):
            print(f"{ch}:{c}")
    """))

Q.append(dict(
    title="Set Report", difficulty="Hard", topics=TOPIC, subTopics=SET,
    prose="Read two lines of space-separated numbers. Print three lines: 'Union: X' "
          "(count of values in either set), 'Intersection: Y' (count in both), and "
          "'Only first: Z' (count in the first but not the second).",
    input_lines=["Line 1: First list", "Line 2: Second list"],
    inputs=["1 2 3 4\n3 4 5", "1 2\n3 4", "1 2 3\n1 2 3", "0\n0", "1 2 3\n4 5 6", "-1 -2\n-2 -3", "1 2 3 4 5 6 7 8\n4 5 6 7 8 9 10"],
    solution="""
        a = set(map(int, input().split()))
        b = set(map(int, input().split()))
        print(f"Union: {len(a | b)}")
        print(f"Intersection: {len(a & b)}")
        print(f"Only first: {len(a - b)}")
    """))

Q.append(dict(
    title="Group by Length", difficulty="Hard", topics=TOPIC, subTopics=DICT,
    prose="Read a sentence and group its words by length. For each length in "
          "ascending order, print 'length: ' followed by the words of that length "
          "in order of appearance, separated by spaces.",
    input_lines=["Line 1: A sentence"],
    inputs=["cat dog fish bird a", "hi hey", "one two six", "x", "aa bb cc", "a bb ccc dddd eeeee", "cat bat hat mat sat pat"],
    solution="""
        words = input().split()
        groups = {}
        for w in words:
            groups.setdefault(len(w), []).append(w)
        for length in sorted(groups):
            print(f"{length}: {' '.join(groups[length])}")
    """))

Q.append(dict(
    title="Common Keys Summed", difficulty="Hard", topics=TOPIC, subTopics=DICT,
    prose="Read two dictionaries of 'key value' pairs. For each key present in both, "
          "print 'key:sum' where sum adds the two values, with keys sorted "
          "alphabetically.",
    input_lines=["Line 1: N", "Next N lines: 'key value'", "Then: M",
                 "Next M lines: 'key value'"],
    inputs=["2\na 1\nb 2\n2\nb 3\nc 4", "1\nx 5\n1\nx 10", "2\np 1\nq 2\n1\nq 8", "0\n0", "1\na 1\n0", "0\n1\nx 5", "3\na 1\nb 2\nc 3\n3\na 10\nb 20\nc 30"],
    solution="""
        first = {}
        n = int(input())
        for _ in range(n):
            key, value = input().split()
            first[key] = int(value)
        second = {}
        m = int(input())
        for _ in range(m):
            key, value = input().split()
            second[key] = int(value)
        for key in sorted(first):
            if key in second:
                print(f"{key}:{first[key] + second[key]}")
    """))

Q.append(dict(
    title="Majority Element", difficulty="Hard", topics=TOPIC, subTopics=DICT,
    prose="Read a line of space-separated numbers and print the value that appears "
          "more than half the time. If no value has a strict majority, print "
          "'None'.",
    input_lines=["Line 1: Space-separated numbers"],
    inputs=["1 1 1 2 3", "1 2 3 4", "2 2 2 2", "5", "1 1 2 2 3", "-1 -1 -1 -2", "1 1 1 1 1 2 2 2 3 3"],
    solution="""
        nums = list(map(int, input().split()))
        counts = {}
        for x in nums:
            counts[x] = counts.get(x, 0) + 1
        answer = "None"
        for value, c in counts.items():
            if c > len(nums) / 2:
                answer = value
        print(answer)
    """))

Q.append(dict(
    title="Count Anagram Groups", difficulty="Hard", topics=TOPIC, subTopics=SET,
    prose="Read N words and print how many distinct anagram groups they form (words "
          "are in the same group if they use the same letters).",
    input_lines=["Line 1: N", "Next N lines: one word each"],
    inputs=["3\nlisten\nsilent\nhello", "2\nabc\ncba", "3\ncat\ndog\nbird", "0", "1\nsolo", "4\nabc\nbca\ncab\nxyz", "5\nrat\ntar\nart\ncar\narc"],
    solution="""
        n = int(input())
        groups = set()
        for _ in range(n):
            word = input()
            groups.add("".join(sorted(word)))
        print(len(groups))
    """))

Q.append(dict(
    title="Passing Students", difficulty="Hard", topics=TOPIC, subTopics=COMP,
    prose="Read N students, each with a name and a score. Using a dictionary "
          "comprehension, keep only those scoring 40 or more, and print their names "
          "sorted alphabetically, one per line.",
    input_lines=["Line 1: N", "Next N lines: 'name score'"],
    inputs=["3\nasha 80\nkabir 30\nmeera 55", "1\nsam 40", "2\na 90\nb 20", "0", "1\nzed 39", "4\na 40\nb 39\nc 100\nd 0", "5\np 41\nq 42\nr 39\ns 40\nt 38"],
    solution="""
        n = int(input())
        students = {}
        for _ in range(n):
            name, score = input().split()
            students[name] = int(score)
        passed = {name: score for name, score in students.items() if score >= 40}
        for name in sorted(passed):
            print(name)
    """))

Q.append(dict(
    title="Top Customer", difficulty="Hard", topics=TOPIC, subTopics=DICT,
    prose="Read N transactions, each a customer name and an amount. Print the "
          "customer with the highest total spend. If several tie, print the name "
          "that comes first alphabetically.",
    input_lines=["Line 1: N", "Next N lines: 'name amount'"],
    inputs=["4\nasha 100\nkabir 200\nasha 150\nkabir 50", "1\nsam 5",
            "3\na 10\nb 30\na 25", "1\nsolo 0", "2\na 0\nb 0",
            "4\nx 10\ny 10\nz 5\nx 0", "5\np 100\nq 100\nr 50\np 0\nq 0"],
    solution="""
        n = int(input())
        totals = {}
        for _ in range(n):
            name, amount = input().split()
            totals[name] = totals.get(name, 0) + int(amount)
        best = max(totals.values())
        winners = sorted(name for name, t in totals.items() if t == best)
        print(winners[0])
    """))

if __name__ == "__main__":
    out = os.path.abspath(os.path.join(
        os.path.dirname(__file__), "..",
        "Unit 7 - Sets and Dictionaries",
        "Unit 7 - Sets and Dictionaries - Coding Questions.xlsx"))
    os.makedirs(os.path.dirname(out), exist_ok=True)
    main(Q, out)
