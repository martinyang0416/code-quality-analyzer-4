from collections import defaultdict

def main():
    n = input().strip()
    digits = list(n)
    freq = defaultdict(int)
    for d in digits:
        freq[d] += 1

    max_k = 0
    best = None

    for k in range(len(digits), 0, -1):
        f = freq.copy()
        pairs = []
        possible = True

        found = False
        for d1 in '9876543210':
            d2 = str(10 - int(d1))
            if d1 > d2:
                continue
            if d1 == d2:
                if f[d1] >= 2:
  