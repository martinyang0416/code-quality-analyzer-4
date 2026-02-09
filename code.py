n = int(input())
s = input().strip()

# Iterate through each possible position to find the first instance where s[i] < s[i+1]
for i in range(n - 1):
    if s[i] < s[i+1]:
        print(s[:i] + s[i+1:])
        exit()

# If no such position found, remove the last character
print(s[:-1])