from functools import lru_cache

class Solution:
    def longestDecomposition(self, text: str) -> int:
        n = len(text)
        
        @lru_cache(maxsize=None)
        def helper(start, end):
            if start > end:
                return 0
            max_k = 1  # Default is the entire substring as one part
            max_possible_l = (end - start + 1) // 2
            for l in range(1, max_possible_l + 1):
                if text[start:start+l] == text[end - l + 1:end + 1]:
       