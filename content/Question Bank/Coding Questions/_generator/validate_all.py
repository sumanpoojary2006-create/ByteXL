"""Re-open every generated xlsx and re-run each solution against its stored
testcase inputs, confirming the stored outputs match (defense-in-depth)."""
import glob, os, subprocess, sys, openpyxl

BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
H = None


def run(code, stdin):
    p = subprocess.run([sys.executable, "-c", code], input=stdin,
                       capture_output=True, text=True, timeout=15)
    if p.returncode != 0:
        return None, p.stderr.strip().splitlines()[-1] if p.stderr else "crash"
    lines = p.stdout.split("\n")
    while lines and lines[-1].strip() == "":
        lines.pop()
    return "\n".join(l.rstrip() for l in lines), None


total_q = total_tc = fails = 0
for path in sorted(glob.glob(os.path.join(BASE, "Unit *", "*Coding Questions.xlsx"))):
    if "backup" in path:
        continue
    ws = openpyxl.load_workbook(path).active
    rows = list(ws.iter_rows(values_only=True))
    hdr = {name: i for i, name in enumerate(rows[0])}
    tc_numbers = sorted({
        int(name[len("testcase"):-len("_input")])
        for name in hdr if name and name.startswith("testcase") and name.endswith("_input")
    })
    unit = os.path.basename(os.path.dirname(path))
    ufails = 0
    for r in rows[1:]:
        total_q += 1
        code = r[hdr["solution_python"]]
        ignore = bool(r[hdr["ignoreCase"]])
        for tc in tc_numbers:
            if r[hdr[f"testcase{tc}_input"]] is None and r[hdr[f"testcase{tc}_output"]] is None:
                continue
            total_tc += 1
            inp = r[hdr[f"testcase{tc}_input"]] or ""
            expected = r[hdr[f"testcase{tc}_output"]] or ""
            got, err = run(code, inp)
            if err is not None:
                fails += 1; ufails += 1
                print(f"CRASH  {unit} | {r[hdr['title']]} tc{tc}: {err}")
                continue
            a, b = (got, expected)
            if ignore:
                a, b = a.lower(), b.lower()
            if a != b:
                fails += 1; ufails += 1
                print(f"MISMATCH {unit} | {r[hdr['title']]} tc{tc}: got={got!r} exp={expected!r}")
    if int(os.path.basename(path).split()[1]) not in (1, 2, 3):
        print(f"OK  {unit}: {len(rows)-1} questions, all testcases pass"
              if ufails == 0 else f"** {unit}: {ufails} failures")

print(f"\n=== {total_q} questions, {total_tc} testcases checked, {fails} failures ===")
