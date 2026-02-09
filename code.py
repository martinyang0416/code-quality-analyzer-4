S = input().strip()
n = len(S)
max_num = 0

for a in range(n):
    current_letters = 0
    pos = -1
    for b in range(a, n):
        if S[b].isalpha():
            current_letters += 1
            if current_letters == 1:
                pos = b
            else:
                break  # More than one letter, stop this a's loop
        if current_letters > 1:
            break
        # Generate candidate
        if current_letters == 0:
            candidate = S[a:b+1]
        else:
          