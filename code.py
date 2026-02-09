import sys

def main():
    input = sys.stdin.read().split()
    idx = 0
    T = int(input[idx])
    idx += 1
    for _ in range(T):
        N = int(input[idx])
        idx +=1
        nums = list(map(int, input[idx:idx+N]))
        idx +=N
        total = sum(nums)
        if total % 2 == 0:
            print("Yes")
        else:
            print("No")

if __name__ == "__main__":
    main()