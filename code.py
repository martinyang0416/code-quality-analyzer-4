def is_palindrome(s):
    return s == s[::-1]

T = int(input())
for _ in range(T):
    s = input().strip()
    if is_palindrome(s):
        print("YES")
        continue
    left = 0
    right = len(s) - 1
    found = False
    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            # Check two possibilities: delete left or delete right
            s1 = s[left+1 : right+1]  # Delete left character
            s2 = s[left : right]