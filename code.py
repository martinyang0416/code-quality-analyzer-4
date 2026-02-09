n = int(input())
ages = list(map(int, input().split()))

evens = []
odds = []

for idx in range(n):
    if ages[idx] % 2 == 0:
        evens.append(idx + 1)  # Using 1-based index
    else:
        odds.append(idx + 1)

even_count = len(evens)
odd_count = len(odds)

impossible = False
if even_count > 0 and even_count < 4:
    impossible = True
if odd_count > 0 and odd_count < 4:
    impossible = True

if impossible:
    print("Impossible")
else:
    tables = []
    if even_count >= 4:
        ta