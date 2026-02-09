n, r = map(int, input().split())
f_list = list(map(int, input().split()))
e_list = list(map(int, input().split()))

deltas = [f - r * e for f, e in zip(f_list, e_list)]

dp = {0: 0}  # Maps sum of deltas to the maximum sum of e

for delta, e in zip(deltas, e_list):
    current_states = list(dp.items())
    for s, current_e in current_states:
        new_s = s + delta
        new_e = current_e + e
        if new_s in dp:
            if new_e > dp[new_s]:
                dp[new_s] = new_e
        