"""Reference solution, Unit 2 mini project: campus route planner."""
import heapq, math

# Goal sits far east. A cluster of cheap paths runs west, away from the goal:
# uniform cost explores them because they are cheap, A star skips them.
COORDS = {
    "Main Gate": (0, 0),  "Parking": (-2, 1),  "Workshop": (-3, -1),
    "Store": (-1, -2),    "Guest House": (-4, 1), "Pump House": (-5, -1),
    "Nursery": (-3, 3),   "Old Block": (-6, 2),  "Canteen": (1, 2),
    "Riverside": (8, 5),
    "Library": (3, 1),    "Admin": (2, 4),     "Block A": (5, 2),
    "Hostel": (4, 5),     "Block B": (7, 3),   "Sports Ground": (9, 4),
}
ROADS = [
    ("Main Gate", "Parking", 3), ("Main Gate", "Store", 3), ("Main Gate", "Canteen", 3),
    ("Parking", "Workshop", 3),  ("Parking", "Guest House", 3), ("Workshop", "Store", 3),
    ("Guest House", "Pump House", 3), ("Guest House", "Nursery", 3),
    ("Guest House", "Old Block", 3),  ("Workshop", "Pump House", 3),
    ("Canteen", "Library", 3),   ("Canteen", "Admin", 3),
    ("Library", "Block A", 3),   ("Admin", "Hostel", 3),
    ("Block A", "Block B", 3),   ("Hostel", "Block B", 4),
    ("Block B", "Sports Ground", 3),
    # Riverside is close to the goal in a straight line and far by road:
    # the trap that greedy search walks into.
    ("Canteen", "Riverside", 8), ("Riverside", "Sports Ground", 12),
]
GRAPH = {}
for a, b, w in ROADS:
    GRAPH.setdefault(a, []).append((b, w))
    GRAPH.setdefault(b, []).append((a, w))

def straight_line(a, b):
    (x1, y1), (x2, y2) = COORDS[a], COORDS[b]
    return math.hypot(x1 - x2, y1 - y2)

# Admissibility precondition: no road may be shorter than the straight line.
bad = [(a, b) for a, b, w in ROADS if w < straight_line(a, b) - 1e-9]
assert not bad, f"heuristic would overestimate on {bad}"

def search(start, goal, mode):
    """mode: 'ucs' orders by cost so far, 'greedy' by estimate remaining,
    'astar' by their sum."""
    frontier = [(0.0, 0.0, start, [start])]
    settled, expanded = set(), []
    while frontier:
        _, cost, node, path = heapq.heappop(frontier)
        if node in settled:
            continue
        settled.add(node); expanded.append(node)
        if node == goal:
            return path, cost, expanded
        for nxt, w in GRAPH[node]:
            if nxt in settled:
                continue
            g = cost + w
            h = straight_line(nxt, goal)
            key = {"ucs": g, "greedy": h, "astar": g + h}[mode]
            heapq.heappush(frontier, (key, g, nxt, path + [nxt]))
    return None, float("inf"), expanded

START, GOAL = "Main Gate", "Sports Ground"
print(f"Planning a route from {START} to {GOAL}")
print(f"Campus has {len(COORDS)} locations and {len(ROADS)} paths")
print()
results = {}
for name, mode in (("Uniform cost", "ucs"), ("Greedy best-first", "greedy"), ("A star", "astar")):
    path, cost, expanded = search(START, GOAL, mode)
    results[name] = (path, cost, expanded)
    print(f"{name}")
    print(f"   route     {' -> '.join(path)}")
    print(f"   cost      {cost:.0f}")
    print(f"   expanded  {len(expanded)} locations")
    print()

u_path, u_cost, u_exp = results["Uniform cost"]
g_path, g_cost, g_exp = results["Greedy best-first"]
a_path, a_cost, a_exp = results["A star"]
print(f"A star matches the uniform-cost route: {u_path == a_path}, cost {a_cost:.0f}")
print(f"A star expanded {len(u_exp) - len(a_exp)} fewer locations than uniform cost")
print("Skipped by A star: " + ", ".join(sorted(set(u_exp) - set(a_exp))))
print(f"Greedy cost {g_cost:.0f} against the best {u_cost:.0f}: "
      f"{'optimal here' if g_cost == u_cost else 'NOT optimal'}")
