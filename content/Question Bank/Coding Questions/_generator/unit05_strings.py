"""Unit 5 - Strings - Coding Questions (30: 10/10/10).

Scope: indexing & slicing, immutability, string methods, split/join, searching,
f-strings/formatting, escape sequences, practical text processing.
"""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from cqlib import main

TOPIC = "strings"
IDX, METH, FMT = "indexing-slicing", "string-methods", "formatting"

Q = []

# ----------------------------- EASY (10) -----------------------------
Q.append(dict(
    title="Shout It Out", difficulty="Easy", topics=TOPIC, subTopics=METH,
    prose="A chat app has a 'caps' button. Read one line of text and print it "
          "entirely in upper case.",
    input_lines=["Line 1: A line of text"],
    inputs=["hello world", "Python", "abc", "a", "ALREADY UPPER", "MiXeD CaSe 123", "the quick brown fox jumps"],
    solution="""
        text = input()
        print(text.upper())
    """))

Q.append(dict(
    title="First and Last", difficulty="Easy", topics=TOPIC, subTopics=IDX,
    prose="Read a word and print its first and last characters separated by a "
          "space. A one-letter word uses the same character for both.",
    input_lines=["Line 1: A word"],
    inputs=["python", "a", "hello", "ab", "z", "programming", "x9y"],
    solution="""
        word = input()
        print(word[0], word[-1])
    """))

Q.append(dict(
    title="Message Length", difficulty="Easy", topics=TOPIC, subTopics=METH,
    prose="A text box shows a character counter. Read one line and print how many "
          "characters it contains.",
    input_lines=["Line 1: A line of text"],
    inputs=["hello", "coding", "a", "\n", "   ", "supercalifragilisticexpialidocious", "x y z"],
    solution="""
        text = input()
        print(len(text))
    """))

Q.append(dict(
    title="Preview Snippet", difficulty="Easy", topics=TOPIC, subTopics=IDX,
    prose="A search result shows only the first 3 characters of a title as a "
          "preview. Read a title and print its first 3 characters (or the whole "
          "title if it is shorter).",
    input_lines=["Line 1: A title"],
    inputs=["introduction", "cat", "hi", "a", "abc", "byte", "This Is A Long Title"],
    solution="""
        title = input()
        print(title[:3])
    """))

Q.append(dict(
    title="Make a Slug", difficulty="Easy", topics=TOPIC, subTopics=METH,
    prose="A blog turns a title into a URL slug by lower-casing it and replacing "
          "spaces with hyphens. Read a title and print its slug.",
    input_lines=["Line 1: A title"],
    inputs=["Hello World", "Python Is Fun", "ByteXL", "a", "  spaced  edges  ", "ALREADY-HYPHENATED", "one two three four five"],
    solution="""
        title = input()
        print(title.replace(" ", "-").lower())
    """))

Q.append(dict(
    title="Word Count", difficulty="Easy", topics=TOPIC, subTopics=METH,
    prose="A writing tool counts words. Read a line of text and print how many "
          "words it contains (words are separated by spaces).",
    input_lines=["Line 1: A line of text"],
    inputs=["the quick brown fox", "hello", "a b c d", "\n", "   ", "one", "a  b   c    d     e"],
    solution="""
        text = input()
        print(len(text.split()))
    """))

Q.append(dict(
    title="Proper Name", difficulty="Easy", topics=TOPIC, subTopics=METH,
    prose="A form tidies a name so each word starts with a capital letter. Read a "
          "name and print it in title case.",
    input_lines=["Line 1: A name"],
    inputs=["john doe", "mary jane watson", "alice", "a", "MARY JANE", "mcdonald o'brien", "anne marie de la cruz"],
    solution="""
        name = input()
        print(name.title())
    """))

Q.append(dict(
    title="Trim the Fat", difficulty="Easy", topics=TOPIC, subTopics=METH,
    prose="A field removes accidental spaces at the start and end of input. Read a "
          "line, strip the surrounding spaces, and print the result inside square "
          "brackets, like [text].",
    input_lines=["Line 1: A line of text with possible surrounding spaces"],
    inputs=["  hello  ", "   spaced out   ", "clean", "a", "\n", "     ", "  multiple   inner words here  "],
    solution="""
        text = input()
        print("[" + text.strip() + "]")
    """))

Q.append(dict(
    title="Echo Chamber", difficulty="Easy", topics=TOPIC, subTopics=METH,
    prose="A sound effect repeats a short sound N times. Read the text, then N, and "
          "print the text repeated N times with no spaces between copies.",
    input_lines=["Line 1: The text", "Line 2: N, the number of repeats"],
    inputs=["ab\n3", "x\n5", "hi\n1", "a\n0", "hello\n2", "z\n10", "ab\n100"],
    solution="""
        text = input()
        n = int(input())
        print(text * n)
    """))

Q.append(dict(
    title="Initials", difficulty="Easy", topics=TOPIC, subTopics=IDX,
    prose="A badge printer shows a person's initials. Read a full name and print "
          "the capitalised first letter of each word joined together.",
    input_lines=["Line 1: A full name"],
    inputs=["john ronald tolkien", "alan turing", "grace", "a", "mary jane watson parker", "already Upper Case", "a b c d e f g"],
    solution="""
        name = input()
        initials = ""
        for word in name.split():
            initials += word[0].upper()
        print(initials)
    """))

# ----------------------------- MEDIUM (10) -----------------------------
Q.append(dict(
    title="Palindrome Check", difficulty="Medium", topics=TOPIC, subTopics=IDX,
    prose="Read a word and print 'Yes' if it reads the same forwards and backwards "
          "(ignoring case), otherwise print 'No'.",
    input_lines=["Line 1: A word"],
    inputs=["racecar", "Hello", "Level", "a", "\n", "Noon", "abcba"],
    solution="""
        word = input().lower()
        print("Yes" if word == word[::-1] else "No")
    """))

Q.append(dict(
    title="Word Reverser", difficulty="Medium", topics=TOPIC, subTopics=METH,
    prose="Read a sentence and print its words in reverse order, separated by "
          "single spaces.",
    input_lines=["Line 1: A sentence"],
    inputs=["hello world", "one two three", "single", "a b", "the quick brown fox jumps over", "x", "  extra   spaces   here  "],
    solution="""
        words = input().split()
        print(" ".join(words[::-1]))
    """))

Q.append(dict(
    title="Swap Case", difficulty="Medium", topics=TOPIC, subTopics=METH,
    prose="A novelty keyboard swaps the case of every letter. Read a line and print "
          "it with upper-case letters made lower-case and vice versa.",
    input_lines=["Line 1: A line of text"],
    inputs=["Hello World", "PyThOn", "abcXYZ", "a", "\n", "ALLCAPS", "1234 mixed CASE 5678"],
    solution="""
        text = input()
        print(text.swapcase())
    """))

Q.append(dict(
    title="Find the Word", difficulty="Medium", topics=TOPIC, subTopics=METH,
    prose="Read a line of text, then a word to search for. Print the index where "
          "the word first appears, or -1 if it does not appear.",
    input_lines=["Line 1: A line of text", "Line 2: The word to find"],
    inputs=["hello world\nworld", "abcabc\nbc", "python\nxyz", "a\na", "hello\n\n", "aaaa\naa", "the quick brown fox\nbrown"],
    solution="""
        text = input()
        word = input()
        print(text.find(word))
    """))

Q.append(dict(
    title="Count Substring", difficulty="Medium", topics=TOPIC, subTopics=METH,
    prose="Read a line of text, then a smaller piece of text. Print how many times "
          "the piece appears in the line (non-overlapping).",
    input_lines=["Line 1: A line of text", "Line 2: The piece to count"],
    inputs=["banana\na", "aaaa\naa", "hello\nz", "a\na", "mississippi\nss", "aaaaaa\naaa", "hello world\n "],
    solution="""
        text = input()
        piece = input()
        print(text.count(piece))
    """))

Q.append(dict(
    title="Censor a Word", difficulty="Medium", topics=TOPIC, subTopics=METH,
    prose="A chat filter replaces a banned word with '***'. Read a line of text, "
          "then the banned word, and print the line with every occurrence "
          "replaced.",
    input_lines=["Line 1: A line of text", "Line 2: The banned word"],
    inputs=["this is bad\nbad", "spam spam eggs\nspam", "clean text\ndirty", "a\na", "bad bad bad\nbad", "hello world\nworld", "no match here\nzzz"],
    solution="""
        text = input()
        word = input()
        print(text.replace(word, "***"))
    """))

Q.append(dict(
    title="Email Domain", difficulty="Medium", topics=TOPIC, subTopics=METH,
    prose="Read an email address and print just the domain part that comes after "
          "the '@' sign.",
    input_lines=["Line 1: An email address"],
    inputs=["john@example.com", "a.b@mail.co.in", "user@site.org", "x@y.co", "first.last@sub.domain.com", "a1@test123.net", "name@company.io"],
    solution="""
        email = input()
        print(email.split("@")[1])
    """))

Q.append(dict(
    title="Receipt Line", difficulty="Medium", topics=TOPIC, subTopics=FMT,
    prose="A till prints a receipt line. Read an item name, a quantity, and a unit "
          "price, then print a line like 'Coffee x 3 = 7.50' with the total shown "
          "to exactly 2 decimal places.",
    input_lines=["Line 1: Item name", "Line 2: Quantity", "Line 3: Unit price"],
    inputs=["Coffee\n3\n2.5", "Tea\n1\n1.0", "Cake\n2\n4.75", "Water\n0\n1.5", "Muffin\n1\n0", "Soda\n10\n1.99", "Sandwich\n7\n3.333"],
    solution="""
        item = input()
        qty = int(input())
        price = float(input())
        print(f"{item} x {qty} = {qty * price:.2f}")
    """))

Q.append(dict(
    title="Mask a Card", difficulty="Medium", topics=TOPIC, subTopics=IDX,
    prose="A payment page hides all but the last 4 digits of a card number, showing "
          "an asterisk for each hidden digit. Read the number and print the masked "
          "version.",
    input_lines=["Line 1: A card number (digits only)"],
    inputs=["1234567812345678", "0000111122223333", "4444", "1234", "12345", "9999888877776666", "1111222233334444555566667777"],
    solution="""
        card = input()
        print("*" * (len(card) - 4) + card[-4:])
    """))

Q.append(dict(
    title="Starts With", difficulty="Medium", topics=TOPIC, subTopics=METH,
    prose="Read a line of text, then a prefix. Print 'Yes' if the text starts with "
          "that prefix, otherwise print 'No'.",
    input_lines=["Line 1: A line of text", "Line 2: The prefix"],
    inputs=["python\npy", "hello\nhi", "coding\ncod", "a\na", "hello\n\n", "abc\nabcd", "the quick fox\nthe quick"],
    solution="""
        text = input()
        prefix = input()
        print("Yes" if text.startswith(prefix) else "No")
    """))

# ----------------------------- HARD (10) -----------------------------
Q.append(dict(
    title="Vowels and Consonants", difficulty="Hard", topics=TOPIC, subTopics=METH,
    prose="Read a line of text and print two numbers: how many vowels and how many "
          "consonants it contains, separated by a space. Count letters only and "
          "ignore case.",
    input_lines=["Line 1: A line of text"],
    inputs=["education", "xyz", "AEIOU bcd", "a", "bcdfg", "The Quick Brown Fox", "aaaaaeeeee"],
    solution="""
        text = input().lower()
        vowels = consonants = 0
        for ch in text:
            if ch.isalpha():
                if ch in "aeiou":
                    vowels += 1
                else:
                    consonants += 1
        print(vowels, consonants)
    """))

Q.append(dict(
    title="Most Frequent Character", difficulty="Hard", topics=TOPIC, subTopics=METH,
    prose="Read a line of text and print the character that appears most often. If "
          "several characters tie, print the one that appears earliest in the text.",
    input_lines=["Line 1: A line of text (no spaces)"],
    inputs=["mississippi", "aabbbcc", "hello", "a", "abcabc", "zzzzzzz", "abcdefgghh"],
    solution="""
        text = input()
        best = ""
        best_count = 0
        for ch in text:
            count = text.count(ch)
            if count > best_count:
                best_count = count
                best = ch
        print(best)
    """))

Q.append(dict(
    title="Caesar Cipher", difficulty="Hard", topics=TOPIC, subTopics=IDX,
    prose="Encrypt a message by shifting each lower-case letter forward by K places "
          "in the alphabet, wrapping from z back to a. Non-letters stay unchanged. "
          "Read the message and K, then print the encrypted text.",
    input_lines=["Line 1: The message (lower-case)", "Line 2: K, the shift"],
    inputs=["abc\n1", "xyz\n3", "hello\n5", "a\n0", "hello world\n1", "abc xyz\n26", "z\n25"],
    solution="""
        text = input()
        k = int(input())
        result = ""
        for ch in text:
            if ch.isalpha():
                result += chr((ord(ch) - 97 + k) % 26 + 97)
            else:
                result += ch
        print(result)
    """))

Q.append(dict(
    title="Word Frequency", difficulty="Hard", topics=TOPIC, subTopics=METH,
    prose="Read a sentence and, for each distinct word in order of first "
          "appearance, print the word and how many times it appears, separated by "
          "a space, one per line.",
    input_lines=["Line 1: A sentence"],
    inputs=["a b a c b a", "hello hello", "one two two three three three", "a", "x y z", "same same same same", "a b c a b c a b c a"],
    solution="""
        words = input().split()
        seen = []
        for w in words:
            if w not in seen:
                seen.append(w)
        for w in seen:
            print(w, words.count(w))
    """))

Q.append(dict(
    title="Make an Acronym", difficulty="Hard", topics=TOPIC, subTopics=METH,
    prose="Read a phrase and print its acronym: the capitalised first letter of "
          "each word, joined together.",
    input_lines=["Line 1: A phrase"],
    inputs=["random access memory", "portable document format", "as soon as possible", "a", "hello world", "already Capitalized Words", "a b c d e f g h"],
    solution="""
        words = input().split()
        acronym = ""
        for w in words:
            acronym += w[0].upper()
        print(acronym)
    """))

Q.append(dict(
    title="Remove Duplicate Characters", difficulty="Hard", topics=TOPIC, subTopics=IDX,
    prose="Read a word and print it with duplicate characters removed, keeping only "
          "the first occurrence of each character in order.",
    input_lines=["Line 1: A word"],
    inputs=["programming", "aabbcc", "abcabc", "a", "aaaaaaa", "abcdef", "mississippi"],
    solution="""
        word = input()
        result = ""
        for ch in word:
            if ch not in result:
                result += ch
        print(result)
    """))

Q.append(dict(
    title="Anagram Check", difficulty="Hard", topics=TOPIC, subTopics=METH,
    prose="Read two lines of text and print 'Yes' if they are anagrams of each "
          "other (same letters in any order), ignoring case and spaces; otherwise "
          "print 'No'.",
    input_lines=["Line 1: First text", "Line 2: Second text"],
    inputs=["listen\nsilent", "hello\nworld", "Dormitory\nDirty Room", "a\na", "abc\ncba", "aabbcc\nabcabc", "The Morse Code\nHere Come Dots"],
    solution="""
        a = input().lower().replace(" ", "")
        b = input().lower().replace(" ", "")
        print("Yes" if sorted(a) == sorted(b) else "No")
    """))

Q.append(dict(
    title="Run-Length Encoding", difficulty="Hard", topics=TOPIC, subTopics=IDX,
    prose="Compress a word by replacing runs of the same character with the "
          "character followed by how many times it repeats. For example 'aaabbc' "
          "becomes 'a3b2c1'. Read a word and print its compressed form.",
    input_lines=["Line 1: A word"],
    inputs=["aaabbc", "abc", "wwwwww", "a", "aabbccddee", "z", "aaaaaaaaaabbbbbbbbbb"],
    solution="""
        word = input()
        result = ""
        i = 0
        while i < len(word):
            ch = word[i]
            count = 1
            while i + count < len(word) and word[i + count] == ch:
                count += 1
            result += ch + str(count)
            i += count
        print(result)
    """))

Q.append(dict(
    title="Longest Word", difficulty="Hard", topics=TOPIC, subTopics=METH,
    prose="Read a sentence and print its longest word. If several words tie for the "
          "longest, print the one that appears first.",
    input_lines=["Line 1: A sentence"],
    inputs=["the quick brown fox", "i love programming", "a bb ccc dd", "a", "same size word test", "a bb aa cc", "supercalifragilistic is long but hi is not"],
    solution="""
        words = input().split()
        best = words[0]
        for w in words[1:]:
            if len(w) > len(best):
                best = w
        print(best)
    """))

Q.append(dict(
    title="Last Name First", difficulty="Hard", topics=TOPIC, subTopics=FMT,
    prose="A directory lists people as 'Last, First'. Read N, then N lines each with "
          "a first and last name separated by a space, and print each name "
          "reformatted as 'Last, First', one per line.",
    input_lines=["Line 1: N", "Next N lines: 'first last'"],
    inputs=["2\njohn doe\nmary jane", "1\nalice smith", "3\na b\nc d\ne f", "1\nx y", "0", "4\na b\nc d\ne f\ng h", "2\njohn ronald\nmary jane"],
    solution="""
        n = int(input())
        for _ in range(n):
            first, last = input().split()
            print(f"{last}, {first}")
    """))

if __name__ == "__main__":
    out = os.path.abspath(os.path.join(
        os.path.dirname(__file__), "..",
        "Unit 5 - Strings", "Unit 5 - Strings - Coding Questions.xlsx"))
    os.makedirs(os.path.dirname(out), exist_ok=True)
    main(Q, out)
