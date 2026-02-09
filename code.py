from typing import List

class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if n < d:
            return -1
        
        INF = float('inf')
        dp = [[INF] * (d + 1) for _ in range(n + 1)]
        dp[0][0] = 0
        
        for k in range(1, d + 1):
            for i in range(k, n + 1):
                if k == 1:
                    dp[i][k] = max(jobDifficulty[:i])
                else:
                    curr