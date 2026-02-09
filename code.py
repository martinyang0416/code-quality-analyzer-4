n = int(input())
scores = list(map(int, input().split()))
sorted_scores = sorted(scores, reverse=True)
rank_dict = {}

for i, s in enumerate(sorted_scores):
    if s not in rank_dict:
        rank_dict[s] = i + 1

print("Yes")
for s in scores:
    print(rank_dict[s])