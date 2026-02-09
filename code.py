import math
import itertools

n = int(input())
radii = [int(input()) for _ in range(n)]

max_circumference = 0.0

for k in range(3, n + 1):
    for subset in itertools.combinations(radii, k):
        sum_r = sum(subset)
        for arrangement in itertools.permutations(subset):
            valid = True
            for i in range(k):
                a = arrangement[i]
                b = arrangement[(i + 1) % k]
                if a + b >= sum_r:
                    valid = False
                