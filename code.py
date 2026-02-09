def main():
    import sys
    input = sys.stdin.read().split()
    idx = 0
    n = int(input[idx])
    idx += 1
    r1 = int(input[idx])
    idx += 1
    r2 = int(input[idx])
    idx += 1
    r3 = int(input[idx])
    idx += 1
    d = int(input[idx])
    idx += 1
    a = list(map(int, input[idx:idx+n]))
    
    total = 0
    movement = (n - 1) * d
    for ai in a:
        groups = ai + 1
        blaster = groups * r1
        plasma = r2
        ion = groups * r3
        total += min(blaster, pl