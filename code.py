a = int(input())
s = sum(int(d) for d in str(a))
print("YES" if s % 5 == 0 else "NO")