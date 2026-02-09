def sieve(max_sum):
    if max_sum < 2:
        return [False] * (max_sum + 1)
    is_prime = [True] * (max_sum + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(max_sum ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, max_sum + 1, i):
                is_prime[j] = False
    return is_prime

def main():
    import sys
    input = sys.stdin.read().split()
    N = int(input[0])
    arr = list(map(int, input[1:N+1]))
    
    total = sum(arr)
    if total <