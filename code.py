n = int(input())
scores = list(map(int, input().split()))
min_score = min(scores)
third_student_score = scores[2]
modified_score = (min_score ^ third_student_score) + 5
print(modified_score)