n, c = map(int, input().split())
x = list(map(int, input().split()))
max_profit = max([x[i] - x[i+1] - c for i in range(n-1)] + [0])
print(max_profit if max_profit > 0 else 0)