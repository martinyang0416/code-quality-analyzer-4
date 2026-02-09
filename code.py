def main():
    import sys
    input = sys.stdin.read().split()
    N = int(input[0])
    index = 1
    result = []
    for _ in range(N):
        a, b, c, d, e = map(int, input[index:index+5])
        index +=5
        sum_first = a + b + c
        # Since the problem states the sums are equal, only calculate one
        # The letter is determined by sum_first + 96 (since 'a' is 97 in ASCII)
        # Wait, the first example gives a when sum_first is 1 → 1 corresponds to 'a'
        # So we nee