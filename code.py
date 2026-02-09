n = int(input())
s = input().strip()

if n == 0:
    print("")
    exit()

result = []
current_char = s[0]
count = 1

for i in range(1, n):
    if s[i] == current_char:
        count += 1
    else:
        # Process the current run
        if current_char in {'a', 'e', 'i', 'o', 'u', 'y'}:
            if current_char in {'e', 'o'}:
                if count == 2:
                    result.append(current_char * 2)
                else:
                    result.append(current_char)
            e