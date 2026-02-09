class House:
    c = 0

    def __init__(self, val):
        self.id = House.c + 1
        self.val = int(val)
        House.c += 1

n = int(input())
a = list(map(House, input().split()))
a.sort(key=lambda x: x.val)
length = 0
pos1 = pos2 = 1
for i in range(n * 2):
    if i % 2:
        length += abs(pos2 - a[i].id)
        pos2 = a[i].id
    else:
        length += abs(pos1 - a[i].id)
        pos1 = a[i].id
print(length)