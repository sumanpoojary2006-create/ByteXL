"""Reference solution, Unit 4 mini project: loan screening end to end."""
import random
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.tree import DecisionTreeClassifier
from sklearn.dummy import DummyClassifier
from sklearn.metrics import confusion_matrix

rng = random.Random(7)
# 400 applications. 'officer_note' is deliberately poisoned: it is written
# AFTER the decision, so it leaks the answer.
rows = []
for _ in range(400):
    income = rng.randint(15, 90)
    years = rng.randint(0, 12)
    score = rng.randint(520, 820)
    risk = (score - 520) / 300 * 0.6 + min(years, 8) / 8 * 0.3 + (income - 15) / 75 * 0.1
    approved = 1 if rng.random() < risk else 0
    officer_note = approved if rng.random() < 0.95 else 1 - approved
    rows.append([income, years, score, officer_note, approved])

NAMES = ["income_k", "years_employed", "credit_score", "officer_note"]
X_all = [r[:4] for r in rows]
X_clean = [r[:3] for r in rows]
y = [r[4] for r in rows]
print(f"{len(rows)} applications, {sum(y)} approved ({100*sum(y)/len(y):.0f} percent)")
print()

def evaluate(X, names, label):
    Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.25,
                                          random_state=0, stratify=y)
    m = DecisionTreeClassifier(max_depth=3, random_state=0).fit(Xtr, ytr)
    acc = m.score(Xte, yte)
    imp = {n: round(float(v), 2) for n, v in zip(names, m.feature_importances_)}
    print(f"{label}")
    print(f"   test accuracy       {acc:.3f}")
    print(f"   feature importance  {imp}")
    return acc

a_leak = evaluate(X_all, NAMES, "WITH officer_note (recorded after the decision)")
print()
a_clean = evaluate(X_clean, NAMES[:3], "WITHOUT officer_note")
print()
print(f"Dropping the leaked column costs {a_leak - a_clean:.3f} accuracy.")
print("The higher number was never real; it was the answer copied into a column.")
print()

Xtr, Xte, ytr, yte = train_test_split(X_clean, y, test_size=0.25,
                                      random_state=0, stratify=y)
base = cross_val_score(DummyClassifier(strategy="most_frequent"), Xtr, ytr, cv=5)
print(f"Baseline (always predict the majority)  {base.mean():.3f}")

search = GridSearchCV(DecisionTreeClassifier(random_state=0),
                      {"max_depth": [1, 2, 3, 5, 8, None]}, cv=5)
search.fit(Xtr, ytr)
best = search.best_params_["max_depth"]
print(f"Best max_depth by cross-validation      {best}")
print(f"Cross-validated accuracy                {search.best_score_:.3f}")
print()

tn, fp, fn, tp = confusion_matrix(yte, search.predict(Xte)).ravel()
prec = tp / (tp + fp) if tp + fp else 0.0
rec = tp / (tp + fn) if tp + fn else 0.0
print("TEST SET, opened once")
print(f"   approved and repaid (tp)   {tp:>3}      approved, defaulted (fp) {fp:>3}")
print(f"   rejected, would repay (fn) {fn:>3}      rejected correctly  (tn) {tn:>3}")
print(f"   accuracy {(tp+tn)/len(yte):.3f}   precision {prec:.3f}   recall {rec:.3f}")
