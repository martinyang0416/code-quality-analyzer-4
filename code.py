# Read the two numbers from input
n1 = int(input())
n2 = int(input())

# Check if the first number is greater than the second
if n1 > n2:
    result = n1 - n2
else:
    result = n1 + n2

# Output the result
print(result)