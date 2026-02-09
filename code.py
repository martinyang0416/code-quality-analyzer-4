import sys

def can_reach_end(n, k, r):
    # Check left path
    current = 0
    left_possible = True
    for i in range(k-1, 0, -1):
        current += r[i-1]
        if current < 0:
            left_possible = False
            break
    if left_possible:
        return True
    
    # Check right path
    current = 0
    right_possible = True
    for i in range(k+1, n+1):
        if i > n:
            break
        current += r[i-1]
        if current < 0:
            right_possible = False
