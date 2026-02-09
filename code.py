a, b, c = map(int, input().split())
divisors = [i for i in range(1, c + 1) if c % i == 0]
count = sum(a <= d <= b for d in divisors)
print(count)