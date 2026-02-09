import sys

def main():
    input = sys.stdin.read().split()
    ptr = 0
    T = int(input[ptr])
    ptr += 1
    for _ in range(T):
        N, K = int(input[ptr]), int(input[ptr+1])
        ptr += 2
        count = [0] * (K + 1)
        all_ingredients = set()
        ingredients_list = []
        for _ in range(N):
            Pi = int(input[ptr])
            ptr += 1
            ings = list(map(int, input[ptr:ptr+Pi]))
            ptr += Pi
            ings_set = set(ings)
            ingredi