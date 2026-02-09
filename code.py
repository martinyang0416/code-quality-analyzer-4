import sys

def main():
    input = sys.stdin.read().split()
    idx = 0
    t = int(input[idx])
    idx += 1
    for _ in range(t):
        m = int(input[idx])
        y = int(input[idx+1])
        idx += 2
        b = list(map(int, input[idx:idx+m]))
        idx += m
        
        even_count = 0
        for num in b:
            if num % 2 == 0:
                even_count += 1
        odd_count = m - even_count
        
        # Calculate the minimum and maximum possible number of odds (o)