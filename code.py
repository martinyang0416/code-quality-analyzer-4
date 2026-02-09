def maxArea(h, w, horizontalCuts, verticalCuts):
    MOD = 10**9 + 7
    horizontal = [0] + sorted(horizontalCuts) + [h]
    vertical = [0] + sorted(verticalCuts) + [w]
    max_h = max(y - x for x, y in zip(horizontal, horizontal[1:]))
    max_v = max(y - x for x, y in zip(vertical, vertical[1:]))
    return (max_h * max_v) % MOD