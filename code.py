from itertools import product

def flipLights(n, m):
    if n == 0:
        return 0
    present_classes = set()
    for i in range(1, n + 1):
        parity = i % 2
        mod3 = (i - 1) % 3
        present_classes.add((parity, mod3))
    present_classes = sorted(present_classes)
    unique_states = set()
    
    for a, b, c, d in product([0, 1], repeat=4):
        s = a + b + c + d
        if s > m or (m - s) % 2 != 0:
            continue
        masks = []
        for (p, m3) in present_cl