MOD = 10**9 + 7

def numRollsToTarget(d: int, f: int, target: int) -> int:
    prev = [0] * (target + 1)
    prev[0] = 1  # Base case: 0 dice, sum 0

    for i in range(1, d + 1):
        curr = [0] * (target + 1)
        prefix = [0] * (target + 2)
        # Compute prefix sums of the previous row
        for j in range(target + 1):
            prefix[j + 1] = (prefix[j] + prev[j]) % MOD
        
        for j in range(1, target + 1):
            # The previous sum must be for j - k where k is 