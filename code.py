days_order = {
    'Sunday': 0,
    'Monday': 1,
    'Tuesday': 2,
    'Wednesday': 3,
    'Thursday': 4,
    'Friday': 5,
    'Saturday': 6
}

def main():
    import sys
    input = sys.stdin.read().split('\n')
    ptr = 0
    while True:
        line = input[ptr].strip()
        while not line:
            ptr += 1
            line = input[ptr].strip()
        if line == '0 0':
            break
        N, W = map(int, line.split())
        ptr += 1
        pupils = []
        possible = True
