def find_min_k(s):
    if s == 0:
        return 0
    current_fact = 1
    current_sum = 1
    k = 1
    if current_sum >= s:
        return k
    while True:
        k += 1
        current_fact *= k
        current_sum = sum(int(d) for d in str(current_fact))
        if current_sum >= s:
            return k

T = int(input())
for _ in range(T):
    s = int(input())
    print(find_min_k(s))