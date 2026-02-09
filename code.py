import bisect

def main():
    import sys
    input = sys.stdin.read().split()
    ptr = 0
    T = int(input[ptr])
    ptr += 1
    all_sequences = [
        [],
        ['R'],
        ['Y'],
        ['R', 'R'],
        ['R', 'Y'],
        ['Y', 'R'],
        ['R', 'R', 'Y'],
        ['R', 'Y', 'R'],
        ['Y', 'R', 'R']
    ]
    
    for _ in range(T):
        n = int(input[ptr])
        p = int(input[ptr+1])
        ptr +=2
        m = list(map(int, input[ptr:ptr+n]))
        ptr +=n
     