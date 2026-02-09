from collections import defaultdict

def main():
    import sys
    input = sys.stdin.read().split()
    N = int(input[0])
    M = int(input[1])
    A = list(map(int, input[2:2+N]))
    
    count_dict = defaultdict(int)
    count_dict[0] = 1
    current_sum = 0
    result = 0
    
    for num in A:
        current_sum += num
        rem = current_sum % M
        result += count_dict[rem]
        count_dict[rem] += 1
    
    print(result)

if __name__ == "__main__":
    main()