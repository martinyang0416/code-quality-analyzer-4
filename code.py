n = int(input())
marks = list(map(int, input().split()))
ranks = []
for m in marks:
    count = sum(1 for x in marks if x > m)
    ranks.append(str(count + 1))
print(' '.join(ranks))