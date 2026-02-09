from functools import lru_cache

class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        @lru_cache(maxsize=None)
        def scramble(a, b):
            if a == b:
                return True
            if sorted(a) != sorted(b):
                return False
            n = len(a)
            for k in range(1, n):
                if (scramble(a[:k], b[:k]) and scramble(a[k:], b[k:])) or \
                   (scramble(a[:k], b[-k:]) and scramble(a[k:], b[:-k])):
            