import collections

def max_subsequence_sum(nums, k):
    n = len(nums)
    dp = [0] * n
    dq = collections.deque()
    max_sum = float('-inf')
    
    for i in range(n):
        # Remove indices out of the window [i-k, i-1]
        while dq and dq[0] < i - k:
            dq.popleft()
        
        # Calculate current dp value
        prev_max = dp[dq[0]] if dq else 0
        current = nums[i] + (prev_max if prev_max > 0 else 0)
        dp[i] = current
        
        # Maintain deque in 