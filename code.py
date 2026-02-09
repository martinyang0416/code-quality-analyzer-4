def maxDotProduct(nums1, nums2):
    m, n = len(nums1), len(nums2)
    dp = [[-float('inf')] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = 0  # Base case, but not a valid subsequence
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            current = nums1[i-1] * nums2[j-1]
            # Extend previous subsequences or start new
            option1 = dp[i-1][j-1] + current
            # Just take current pair as a new subsequence
            option2 = current
           