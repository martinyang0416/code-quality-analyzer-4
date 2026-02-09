n = int(input())
cards = list(map(int, input().split()))
left = 0
right = n - 1
sereja = 0
dima = 0
turn = True  # True for Sereja's turn

while left <= right:
    if cards[left] > cards[right]:
        selected = cards[left]
        left += 1
    else:
        selected = cards[right]
        right -= 1
    if turn:
        sereja += selected
    else:
        dima += selected
    turn = not turn

print(sereja, dima)