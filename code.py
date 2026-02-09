n = int(input())
arr = list(map(int, input().split()))

product = 1
for num in arr:
    product *= num
print(product)