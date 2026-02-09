def has_subarray_sum(test_cases):
    for case in test_cases:
        M, Y, arr = case
        current_sum = 0
        seen = {0}
        found = False
        for num in arr:
            current_sum += num
            if (current_sum - Y) in seen:
                found = True
                break
            seen.add(current_sum)
        print("YES" if found else "NO")

def main():
    import sys
    input = sys.stdin.read().split()
    ptr = 0
    K = int(input[ptr])
    ptr += 1
    test_cas