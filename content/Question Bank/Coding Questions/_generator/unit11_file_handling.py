"""Unit 11 - File Handling - Coding Questions (30: 10/10/10).

The coding sandbox has no writable filesystem, so file *content* arrives on
stdin and results go to stdout. Questions exercise the same skills the unit
teaches: reading lines, the csv module, the json module, and pathlib path
handling / glob-style extension matching.
"""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from cqlib import main

TOPIC = "file-handling"
TEXT, CSVT, JSONT = "file-operations", "csv-processing", "json-processing"

Q = []

# ----------------------------- EASY (10) -----------------------------
Q.append(dict(
    title="Count Lines", difficulty="Easy", topics=TOPIC, subTopics=TEXT,
    prose="Imagine reading a text file. Read all the lines from input and print how "
          "many lines there are.",
    input_lines=["All lines: the file contents"],
    inputs=["a\nb\nc", "single", "x\ny", "", "a\nb\nc\nd\ne", "one\ntwo", "z"],
    solution="""
        import sys
        lines = sys.stdin.read().splitlines()
        print(len(lines))
    """))

Q.append(dict(
    title="Numbered Lines", difficulty="Easy", topics=TOPIC, subTopics=TEXT,
    prose="Read the lines of a file and print each one prefixed by its line number "
          "starting at 1, in the form 'number: line'.",
    input_lines=["All lines: the file contents"],
    inputs=["apple\nbanana", "one", "a\nb\nc", "x\ny\nz\nw", "solo", "p\nq", "m\nn\no\np\nq"],
    solution="""
        import sys
        for i, line in enumerate(sys.stdin.read().splitlines(), 1):
            print(f"{i}: {line}")
    """))

Q.append(dict(
    title="Word Count of a File", difficulty="Easy", topics=TOPIC, subTopics=TEXT,
    prose="Read all lines of a file and print the total number of words across every "
          "line.",
    input_lines=["All lines: the file contents"],
    inputs=["the quick\nbrown fox", "hello", "a b\nc d e", "one", "a\nb\nc\nd",
            "  spaced   words  ", "x y z\np q"],
    solution="""
        import sys
        text = sys.stdin.read()
        print(len(text.split()))
    """))

Q.append(dict(
    title="CSV Field Count", difficulty="Easy", topics=TOPIC, subTopics=CSVT,
    prose="Read one line of comma-separated values using the csv module and print "
          "how many fields it contains.",
    input_lines=["Line 1: A CSV row"],
    inputs=["a,b,c", "name,age,city,country", "solo", "1,2,3,4,5", "x,",
            "a,b", "p,q,r,s"],
    solution="""
        import csv, sys
        row = next(csv.reader(sys.stdin))
        print(len(row))
    """))

Q.append(dict(
    title="Read a JSON Field", difficulty="Easy", topics=TOPIC, subTopics=JSONT,
    prose="Read one line of JSON describing an object and print the value of its "
          "'name' field.",
    input_lines=["Line 1: A JSON object"],
    inputs=['{"name": "Asha", "age": 20}', '{"name": "Kabir"}',
            '{"name": "Sam", "city": "X"}', '{"name": ""}',
            '{"name": "Meera", "age": 30, "city": "Pune"}',
            '{"name": "A"}', '{"name": "Zed", "age": 5}'],
    solution="""
        import json
        data = json.loads(input())
        print(data["name"])
    """))

Q.append(dict(
    title="File Name from Path", difficulty="Easy", topics=TOPIC, subTopics=TEXT,
    prose="Use pathlib to read a file path and print just the final file name.",
    input_lines=["Line 1: A file path"],
    inputs=["/home/user/file.txt", "docs/report.pdf", "data.csv",
            "file.txt", "/a/b/c/d.py", "/trailing/slash/dir/",
            "/x/y/z/report.final.csv"],
    solution="""
        from pathlib import PurePosixPath
        print(PurePosixPath(input()).name)
    """))

Q.append(dict(
    title="File Extension", difficulty="Easy", topics=TOPIC, subTopics=TEXT,
    prose="Use pathlib to read a file name and print its extension, including the "
          "leading dot (for example '.txt').",
    input_lines=["Line 1: A file name"],
    inputs=["file.txt", "photo.jpeg", "music.mp3", "noext", "archive.tar.gz",
            ".hidden", "report.final.docx"],
    solution="""
        from pathlib import PurePosixPath
        print(PurePosixPath(input()).suffix)
    """))

Q.append(dict(
    title="Shout the File", difficulty="Easy", topics=TOPIC, subTopics=TEXT,
    prose="Read the lines of a file and print each line converted to upper case.",
    input_lines=["All lines: the file contents"],
    inputs=["hello\nworld", "abc", "a\nb", "MiXeD case", "already UPPER",
            "1 2 3\nfour", "x\ny\nz\nw"],
    solution="""
        import sys
        for line in sys.stdin.read().splitlines():
            print(line.upper())
    """))

Q.append(dict(
    title="Character Count", difficulty="Easy", topics=TOPIC, subTopics=TEXT,
    prose="Read the lines of a file and print how many characters there are in "
          "total, not counting the line breaks.",
    input_lines=["All lines: the file contents"],
    inputs=["abc\nde", "hello", "a\nb\nc", "", "x", "one\ntwo\nthree\nfour",
            "  spaced  \nline"],
    solution="""
        import sys
        lines = sys.stdin.read().splitlines()
        print(sum(len(line) for line in lines))
    """))

Q.append(dict(
    title="Reverse the Lines", difficulty="Easy", topics=TOPIC, subTopics=TEXT,
    prose="Read the lines of a file and print them in reverse order (last line "
          "first).",
    input_lines=["All lines: the file contents"],
    inputs=["a\nb\nc", "one", "x\ny", "", "p\nq\nr\ns", "z", "m\nn\no"],
    solution="""
        import sys
        lines = sys.stdin.read().splitlines()
        for line in reversed(lines):
            print(line)
    """))

# ----------------------------- MEDIUM (10) -----------------------------
Q.append(dict(
    title="Sum a CSV Column", difficulty="Medium", topics=TOPIC, subTopics=CSVT,
    prose="A CSV file has a header row 'name,score' followed by data rows. Use "
          "csv.DictReader to print the total of the 'score' column.",
    input_lines=["Line 1: Header 'name,score'", "Next lines: data rows"],
    inputs=["name,score\nasha,80\nkabir,90", "name,score\nsam,50",
            "name,score\na,10\nb,20\nc,30", "name,score\nx,0",
            "name,score\na,-5\nb,10", "name,score\np,100\nq,100\nr,100",
            "name,score"],
    solution="""
        import csv, sys
        total = 0
        for row in csv.DictReader(sys.stdin):
            total += int(row["score"])
        print(total)
    """))

Q.append(dict(
    title="Filter CSV Rows", difficulty="Medium", topics=TOPIC, subTopics=CSVT,
    prose="A CSV file has a header 'name,score'. Use csv.DictReader to print the "
          "names of everyone scoring 40 or more, one per line.",
    input_lines=["Line 1: Header 'name,score'", "Next lines: data rows"],
    inputs=["name,score\nasha,80\nkabir,30\nmeera,55", "name,score\nsam,40",
            "name,score\na,90\nb,20", "name,score\nx,39", "name,score\ny,0",
            "name,score\na,40\nb,40\nc,40", "name,score"],
    solution="""
        import csv, sys
        for row in csv.DictReader(sys.stdin):
            if int(row["score"]) >= 40:
                print(row["name"])
    """))

Q.append(dict(
    title="Sum a JSON List", difficulty="Medium", topics=TOPIC, subTopics=JSONT,
    prose="Read one line of JSON containing a list of numbers and print their sum.",
    input_lines=["Line 1: A JSON list of numbers"],
    inputs=["[1, 2, 3, 4]", "[10]", "[5, 5, 5]", "[]", "[-3, 3]", "[0]",
            "[100, 200, 300]"],
    solution="""
        import json
        numbers = json.loads(input())
        print(sum(numbers))
    """))

Q.append(dict(
    title="Match by Extension", difficulty="Medium", topics=TOPIC, subTopics=TEXT,
    prose="Read N file names, then an extension (without the dot). Print the file "
          "names that end with that extension, in order, one per line.",
    input_lines=["Line 1: N", "Next N lines: file names", "Last line: an extension"],
    inputs=["3\na.txt\nb.py\nc.txt\ntxt", "2\nx.md\ny.md\nmd", "2\np.jpg\nq.png\njpg",
            "0\ntxt", "1\nfile.txt\ntxt", "3\na.txt\nb.txt\nc.txt\npy",
            "4\na.py\nb.txt\nc.py\nd.md\npy"],
    solution="""
        n = int(input())
        names = [input() for _ in range(n)]
        ext = input()
        for name in names:
            if name.endswith("." + ext):
                print(name)
    """))

Q.append(dict(
    title="Build a Path", difficulty="Medium", topics=TOPIC, subTopics=TEXT,
    prose="Read N path segments and join them into a single path using pathlib, "
          "printing the result with '/' separators.",
    input_lines=["Line 1: N", "Next N lines: one path segment each"],
    inputs=["3\nhome\nuser\nfile.txt", "2\ndocs\na.pdf", "1\nreadme",
            "4\na\nb\nc\nd.txt", "1\nsingle", "2\nx\ny", "3\np\nq\nr"],
    solution="""
        from pathlib import PurePosixPath
        n = int(input())
        parts = [input() for _ in range(n)]
        print(PurePosixPath(*parts))
    """))

Q.append(dict(
    title="Longest Line", difficulty="Medium", topics=TOPIC, subTopics=TEXT,
    prose="Read the lines of a file and print the longest line. If several lines "
          "tie for longest, print the one that appears first.",
    input_lines=["All lines: the file contents"],
    inputs=["a\nbbb\ncc", "hello", "one\ntwo\nthree", "x", "aa\nbb\ncc",
            "short\nreallylongline\nmed", "z\nzz\nzzz\nzz"],
    solution="""
        import sys
        lines = sys.stdin.read().splitlines()
        best = lines[0]
        for line in lines[1:]:
            if len(line) > len(best):
                best = line
        print(best)
    """))

Q.append(dict(
    title="Count a Word in a File", difficulty="Medium", topics=TOPIC, subTopics=TEXT,
    prose="The first line is a word to search for. The remaining lines are the file "
          "contents. Print how many times the word appears across those lines.",
    input_lines=["Line 1: The word to search for", "Remaining lines: file contents"],
    inputs=["cat\nthe cat sat\ncat and cat", "x\nx y x\nz", "hi\nhello\nworld",
            "missing\na b c", "cat\ncatapult cat", "a\na a a\na a",
            "dog\nno match here"],
    solution="""
        import sys
        lines = sys.stdin.read().splitlines()
        word = lines[0]
        body = " ".join(lines[1:]).split()
        print(body.count(word))
    """))

Q.append(dict(
    title="Config Lookup", difficulty="Medium", topics=TOPIC, subTopics=TEXT,
    prose="A config file has N lines like 'key=value'. Read N, then the N lines, "
          "then a key to look up. Print the matching value, or 'Not Found'.",
    input_lines=["Line 1: N", "Next N lines: 'key=value'", "Last line: a key"],
    inputs=["2\nhost=localhost\nport=8080\nport", "1\nname=app\nname",
            "2\na=1\nb=2\nz", "0\nkey", "1\nx=1\nx", "3\na=1\nb=2\nc=3\nc",
            "2\nk1=v1\nk2=v2\nk3"],
    solution="""
        n = int(input())
        config = {}
        for _ in range(n):
            key, value = input().split("=")
            config[key] = value
        print(config.get(input(), "Not Found"))
    """))

Q.append(dict(
    title="Write a CSV", difficulty="Medium", topics=TOPIC, subTopics=CSVT,
    prose="Read N records, each a name and an age separated by a space, and write "
          "them out as CSV rows 'name,age' using the csv module.",
    input_lines=["Line 1: N", "Next N lines: 'name age'"],
    inputs=["2\nasha 20\nkabir 21", "1\nsam 19", "2\na 1\nb 2", "0",
            "1\nzed 99", "3\na 1\nb 2\nc 3", "2\nx 0\ny 5"],
    solution="""
        import csv, sys
        writer = csv.writer(sys.stdout)
        n = int(input())
        for _ in range(n):
            name, age = input().split()
            writer.writerow([name, age])
    """))

Q.append(dict(
    title="Unique Lines", difficulty="Medium", topics=TOPIC, subTopics=TEXT,
    prose="Read the lines of a file and print each distinct line once, keeping the "
          "order of first appearance.",
    input_lines=["All lines: the file contents"],
    inputs=["a\nb\na\nc\nb", "x", "one\none", "", "a\na\na\na", "p\nq\nr\np\nq",
            "z\ny\nx"],
    solution="""
        import sys
        seen = []
        for line in sys.stdin.read().splitlines():
            if line not in seen:
                seen.append(line)
        for line in seen:
            print(line)
    """))

# ----------------------------- HARD (10) -----------------------------
Q.append(dict(
    title="Student Report CSV", difficulty="Hard", topics=TOPIC, subTopics=CSVT,
    prose="A CSV has header 'name,m1,m2,m3' and data rows. Print a new CSV with "
          "header 'name,total,average', where average is rounded to 1 decimal "
          "place, one row per student.",
    input_lines=["Line 1: Header 'name,m1,m2,m3'", "Next lines: data rows"],
    inputs=["name,m1,m2,m3\nasha,80,90,100\nkabir,60,60,60",
            "name,m1,m2,m3\nsam,50,50,50", "name,m1,m2,m3\na,10,20,30",
            "name,m1,m2,m3\nzed,0,0,0", "name,m1,m2,m3\nx,100,100,100",
            "name,m1,m2,m3\np,1,2,2\nq,3,3,3", "name,m1,m2,m3"],
    solution="""
        import csv, sys
        reader = csv.DictReader(sys.stdin)
        writer = csv.writer(sys.stdout)
        writer.writerow(["name", "total", "average"])
        for row in reader:
            marks = [int(row["m1"]), int(row["m2"]), int(row["m3"])]
            total = sum(marks)
            average = round(total / 3, 1)
            writer.writerow([row["name"], total, average])
    """))

Q.append(dict(
    title="Sum JSON Values", difficulty="Hard", topics=TOPIC, subTopics=JSONT,
    prose="Read one line of JSON describing an object that maps names to numbers, "
          "and print the total of all the values.",
    input_lines=["Line 1: A JSON object of name to number"],
    inputs=['{"a": 10, "b": 20, "c": 30}', '{"x": 5}', '{"p": 1, "q": 2}',
            '{}', '{"neg": -10, "pos": 10}', '{"z": 0}',
            '{"m": 100, "n": 200, "o": 300}'],
    solution="""
        import json
        data = json.loads(input())
        print(sum(data.values()))
    """))

Q.append(dict(
    title="Most Common Word in File", difficulty="Hard", topics=TOPIC, subTopics=TEXT,
    prose="Read all the lines of a file and print the word that appears most often "
          "across the whole file. If several tie, print the one that appears first.",
    input_lines=["All lines: the file contents"],
    inputs=["the cat\nthe dog\nthe", "hello world", "a b a", "solo",
            "x y x y", "one two three", "cat dog cat bird cat"],
    solution="""
        import sys
        words = sys.stdin.read().split()
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
    title="Group CSV by Category", difficulty="Hard", topics=TOPIC, subTopics=CSVT,
    prose="A CSV has header 'category,amount'. Print each category's total as "
          "'category:total', with categories sorted alphabetically.",
    input_lines=["Line 1: Header 'category,amount'", "Next lines: data rows"],
    inputs=["category,amount\nfood,100\ntravel,50\nfood,30",
            "category,amount\nrent,500", "category,amount\na,5\na,5",
            "category,amount", "category,amount\nx,0",
            "category,amount\nc,-10\nc,20", "category,amount\nz,1\ny,2\nx,3"],
    solution="""
        import csv, sys
        totals = {}
        for row in csv.DictReader(sys.stdin):
            cat = row["category"]
            totals[cat] = totals.get(cat, 0) + int(row["amount"])
        for cat in sorted(totals):
            print(f"{cat}:{totals[cat]}")
    """))

Q.append(dict(
    title="Log Level Counts", difficulty="Hard", topics=TOPIC, subTopics=TEXT,
    prose="A log file has N lines, each starting with a level (INFO, WARN, or "
          "ERROR) followed by a message. Read N, then the lines, and print each "
          "level that appears with its count as 'LEVEL count', sorted "
          "alphabetically by level.",
    input_lines=["Line 1: N", "Next N lines: 'LEVEL message'"],
    inputs=["3\nINFO started\nERROR failed\nINFO done", "2\nWARN x\nWARN y",
            "1\nERROR z", "0", "1\nINFO only",
            "4\nERROR a\nWARN b\nINFO c\nERROR d", "2\nINFO x\nERROR y"],
    solution="""
        n = int(input())
        counts = {}
        for _ in range(n):
            level = input().split()[0]
            counts[level] = counts.get(level, 0) + 1
        for level in sorted(counts):
            print(level, counts[level])
    """))

Q.append(dict(
    title="CSV to JSON", difficulty="Hard", topics=TOPIC, subTopics=JSONT,
    prose="A CSV has a header row followed by data rows. Convert the whole thing to "
          "a JSON list of objects (one object per data row) and print it with "
          "json.dumps.",
    input_lines=["Line 1: Header row", "Next lines: data rows"],
    inputs=["name,age\nasha,20\nkabir,21", "city\nDelhi", "a,b\n1,2\n3,4",
            "name,age", "x,y,z\n1,2,3", "a\nb\nc\nd", "col1,col2\nv1,v2"],
    solution="""
        import csv, json, sys
        rows = list(csv.DictReader(sys.stdin))
        print(json.dumps([dict(row) for row in rows]))
    """))

Q.append(dict(
    title="Average per Name", difficulty="Hard", topics=TOPIC, subTopics=CSVT,
    prose="A CSV has header 'name,score' with possibly several rows per name. Print "
          "each name's average score (rounded to 1 decimal place) as 'name:average', "
          "with names sorted alphabetically.",
    input_lines=["Line 1: Header 'name,score'", "Next lines: data rows"],
    inputs=["name,score\nasha,80\nasha,100\nkabir,60",
            "name,score\nsam,70", "name,score\na,10\nb,20\na,30",
            "name,score\nx,0", "name,score\nz,1\nz,2\nz,3",
            "name,score\na,100\nb,50\nc,75", "name,score"],
    solution="""
        import csv, sys
        scores = {}
        for row in csv.DictReader(sys.stdin):
            scores.setdefault(row["name"], []).append(int(row["score"]))
        for name in sorted(scores):
            values = scores[name]
            print(f"{name}:{round(sum(values) / len(values), 1)}")
    """))

Q.append(dict(
    title="Match Multiple Extensions", difficulty="Hard", topics=TOPIC, subTopics=TEXT,
    prose="Read N file names, then a line of allowed extensions separated by spaces "
          "(no dots). Print the file names whose extension is in the allowed list, "
          "in their original order.",
    input_lines=["Line 1: N", "Next N lines: file names",
                 "Last line: allowed extensions"],
    inputs=["4\na.txt\nb.py\nc.md\nd.txt\ntxt md", "2\nx.jpg\ny.png\npng",
            "3\np.doc\nq.pdf\nr.doc\ndoc pdf", "0\ntxt", "1\nfile.txt\ntxt",
            "3\na.txt\nb.txt\nc.txt\npy", "2\na.tar.gz\nb.zip\ngz zip"],
    solution="""
        from pathlib import PurePosixPath
        n = int(input())
        names = [input() for _ in range(n)]
        allowed = set(input().split())
        for name in names:
            if PurePosixPath(name).suffix[1:] in allowed:
                print(name)
    """))

Q.append(dict(
    title="Word Frequency as JSON", difficulty="Hard", topics=TOPIC, subTopics=JSONT,
    prose="Read a sentence and print a JSON object mapping each word to how many "
          "times it appears, with the keys sorted alphabetically. Use json.dumps "
          "with sort_keys.",
    input_lines=["Line 1: A sentence"],
    inputs=["a b a c", "hello hello world", "x y z", "single",
            "a a a a", "z y x w v", "cat dog cat bird"],
    solution="""
        import json
        words = input().split()
        counts = {}
        for w in words:
            counts[w] = counts.get(w, 0) + 1
        print(json.dumps(counts, sort_keys=True))
    """))

Q.append(dict(
    title="Validate Records", difficulty="Hard", topics=TOPIC, subTopics=TEXT,
    prose="Read N records, each 'name,age'. A record is valid only if the age is a "
          "whole number greater than 0. Print 'valid X invalid Y' with the counts "
          "of valid and invalid records.",
    input_lines=["Line 1: N", "Next N lines: 'name,age'"],
    inputs=["3\nasha,20\nkabir,-5\nsam,abc", "2\na,10\nb,30", "2\nx,0\ny,5",
            "0", "1\nzed,1", "4\na,1\nb,-1\nc,xyz\nd,2", "1\np,0"],
    solution="""
        n = int(input())
        valid = invalid = 0
        for _ in range(n):
            name, age = input().split(",")
            try:
                if int(age) > 0:
                    valid += 1
                else:
                    invalid += 1
            except ValueError:
                invalid += 1
        print(f"valid {valid} invalid {invalid}")
    """))

if __name__ == "__main__":
    out = os.path.abspath(os.path.join(
        os.path.dirname(__file__), "..",
        "Unit 11 - File Handling",
        "Unit 11 - File Handling - Coding Questions.xlsx"))
    os.makedirs(os.path.dirname(out), exist_ok=True)
    main(Q, out)
