"""Reference solution, Unit 6 mini project: review intelligence system."""
import re, math
from collections import Counter

REVIEWS = [
    ("r1", "the biryani was excellent and the service was quick"),
    ("r2", "the biryani arrived hot and on time and was excellent"),
    ("r3", "the delivery was late and the biryani was cold"),
    ("r4", "the delivery was late again and the food was cold and terrible"),
    ("r5", "the dosa was not good and the packaging was terrible"),
    ("r6", "the service was never slow and the dosa arrived hot"),
]
POSITIVE = {"excellent", "quick", "hot", "good", "fresh"}
NEGATIVE = {"late", "cold", "terrible", "slow", "soggy"}
NEGATORS = {"not", "never", "no"}

tokenise = lambda t: re.findall(r"[a-z']+", t.lower())
docs = {name: tokenise(text) for name, text in REVIEWS}

# ---- TF-IDF search -------------------------------------------------------
vocab = sorted({w for ws in docs.values() for w in ws})
appears = {w: sum(1 for ws in docs.values() if w in ws) for w in vocab}
idf = {w: math.log(len(docs) / appears[w]) for w in vocab}

def tfidf(ws):
    counts = Counter(ws)
    return {w: (c / len(ws)) * idf[w] for w, c in counts.items()}

def search(query, top=3):
    q = [w for w in tokenise(query) if w in idf]
    scored = []
    for name, ws in docs.items():
        v = tfidf(ws)
        scored.append((sum(v.get(w, 0.0) for w in q), name))
    return sorted(scored, reverse=True)[:top]

# ---- sentiment, with and without negation --------------------------------
def bag_score(ws):
    return sum(w in POSITIVE for w in ws) - sum(w in NEGATIVE for w in ws)

def negation_score(ws):
    score, skip = 0, False
    for first, second in zip(ws, ws[1:] + [""]):
        if skip:
            skip = False; continue
        if first in NEGATORS and second:
            if second in POSITIVE: score -= 1; skip = True
            elif second in NEGATIVE: score += 1; skip = True
        elif first in POSITIVE: score += 1
        elif first in NEGATIVE: score -= 1
    return score

print("REVIEW INTELLIGENCE SYSTEM")
print(f"{len(REVIEWS)} reviews, {len(vocab)} distinct words")
print()
print("1. SEARCH: words in every review score zero, so no stopword list is needed")
for count in (6, 3, 2, 1):
    ws = [w for w in vocab if appears[w] == count]
    if ws:
        print(f"   in {count} reviews, idf {idf[ws[0]]:.3f}   {ws[:6]}")
print()
for q in ("cold delivery", "excellent biryani"):
    hits = ", ".join(f"{n} ({s:.3f})" for s, n in search(q))
    print(f"   query '{q}'  ->  {hits}")
print()

print("2. SENTIMENT: the same reviews, scored two ways")
print()
print(f"{'review':<52} {'bag':>5} {'pairs':>6}  agree")
print("-" * 72)
disagreements = 0
for name, text in REVIEWS:
    b, n = bag_score(docs[name]), negation_score(docs[name])
    agree = "yes" if b == n else "NO"
    disagreements += b != n
    print(f"{text[:52]:<52} {b:>5} {n:>6}  {agree}")
print()
print(f"The two methods disagree on {disagreements} of {len(REVIEWS)} reviews.")
print("Every disagreement is a review containing a negation.")
print()

# ---- 3. rank restaurants, using each scorer in turn ----------------------
RESTAURANT = {"r1": "Anand Bhavan", "r2": "Anand Bhavan", "r3": "Spice Route",
              "r4": "Spice Route", "r5": "Cafe Mysore", "r6": "Cafe Mysore"}

def rank(scorer):
    totals = {}
    for name, _ in REVIEWS:
        totals.setdefault(RESTAURANT[name], []).append(scorer(docs[name]))
    return sorted(((sum(v) / len(v), r) for r, v in totals.items()), reverse=True)

print("3. RANKING: which restaurant would you recommend?")
print()
print(f"{'rank':>5}  {'by bag of words':<28}  {'by word pairs':<28}")
print("-" * 68)
for i, (a, b) in enumerate(zip(rank(bag_score), rank(negation_score)), 1):
    print(f"{i:>5}  {a[1] + f' ({a[0]:+.1f})':<28}  {b[1] + f' ({b[0]:+.1f})':<28}")
print()
same = [a[1] for a in rank(bag_score)] == [b[1] for b in rank(negation_score)]
print(f"Identical ranking from both scorers: {same}")
print("Cafe Mysore's two reviews are scored -2 and +2 by the pairs method and")
print("0 and 0 by the bag. Both averages land on zero, so a real per-review")
print("disagreement vanishes the moment it is averaged.")
