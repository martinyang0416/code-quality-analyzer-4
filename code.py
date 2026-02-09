import sys

def generate_all_pairings():
    all_pairings = []
    numbers = [1, 2, 3, 4, 5, 6]
    
    def backtrack(remaining, current_pairs):
        if not remaining:
            all_pairings.append(current_pairs)
            return
        first = remaining[0]
        for i in range(1, len(remaining)):
            pair = (first, remaining[i])
            new_remaining = remaining[1:i] + remaining[i+1:]
            backtrack(new_remaining, current_pairs + [pair])
    
    backtrack(numbers,