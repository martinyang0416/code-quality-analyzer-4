def main():
    import sys
    N, K, T = map(int, sys.stdin.readline().split())
    A = list(map(int, sys.stdin.readline().split()))
    
    # Initialize the position of each cow
    pos_cow = list(range(N))  # pos_cow[p] = cow at position p
    for _ in range(T):
        current_active = [(a + _) % N for a in A]
        # Get the current cows in those positions
        current_cows = [pos_cow[p] for p in current_active]
        # Rotate them: next_cow[i] = current_cows[i+1], with wrap-around
 