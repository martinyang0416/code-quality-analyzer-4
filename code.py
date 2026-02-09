import sys

def main():
    n, V = map(int, sys.stdin.readline().split())
    w = list(map(int, sys.stdin.readline().split()))
    v = list(map(int, sys.stdin.readline().split()))
    
    deltas = [vi - V for vi in v]
    
    dp = {0: 1}  # Initialize with the empty subset
    
    for delta in deltas:
        new_dp = {}
        for current_sum in dp:
            count = dp[current_sum]
            # Option 1: not taking the current delta
            if current_sum in new_dp:
                