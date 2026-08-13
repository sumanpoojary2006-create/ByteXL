"""Reference solution, Unit 5 mini project: a neural network from scratch."""
import math, random

XOR = [((0, 0), 0), ((0, 1), 1), ((1, 0), 1), ((1, 1), 0)]
sigmoid = lambda z: 1 / (1 + math.exp(-z))


def train(seed, rate, epochs=20000, hidden=2):
    rng = random.Random(seed)
    wh = [[rng.uniform(-1, 1) for _ in range(2)] for _ in range(hidden)]
    bh = [rng.uniform(-1, 1) for _ in range(hidden)]
    wo = [rng.uniform(-1, 1) for _ in range(hidden)]
    bo = rng.uniform(-1, 1)

    def forward(x):
        h = [sigmoid(bh[j] + sum(wh[j][i] * x[i] for i in range(2)))
             for j in range(hidden)]
        return h, sigmoid(bo + sum(wo[j] * h[j] for j in range(hidden)))

    for _ in range(epochs):
        for x, target in XOR:
            h, out = forward(x)
            d_out = (out - target) * out * (1 - out)
            d_h = [d_out * wo[j] * h[j] * (1 - h[j]) for j in range(hidden)]
            for j in range(hidden):
                wo[j] -= rate * d_out * h[j]
            bo -= rate * d_out
            for j in range(hidden):
                for i in range(2):
                    wh[j][i] -= rate * d_h[j] * x[i]
                bh[j] -= rate * d_h[j]

    loss = sum((t - forward(x)[1]) ** 2 for x, t in XOR) / len(XOR)
    correct = sum(round(forward(x)[1]) == t for x, t in XOR)
    return loss, correct


print("A NEURAL NETWORK FROM SCRATCH: 2-2-1 on XOR")
print()
print("Does the starting point matter? Same code, same data, 8 seeds, rate 0.5")
print()
print(f"{'seed':>5} {'final loss':>12} {'cases right':>12}  verdict")
print("-" * 48)
solved = 0
for seed in range(8):
    loss, correct = train(seed, 0.5)
    ok = correct == 4 and loss < 0.01
    solved += ok
    print(f"{seed:>5} {loss:>12.5f} {correct:>9}/4  {'solved' if ok else 'STUCK'}")
print()
print(f"{solved} of 8 seeds solved XOR. The rest reached a hollow they could not leave.")
print()

print("Does the learning rate matter? Seed 1 throughout, which solves at 0.5")
print()
print(f"{'rate':>7} {'final loss':>12} {'cases right':>12}")
print("-" * 34)
for rate in (0.001, 0.01, 0.1, 0.5, 5.0, 50.0):
    loss, correct = train(1, rate)
    print(f"{rate:>7} {loss:>12.5f} {correct:>9}/4")
