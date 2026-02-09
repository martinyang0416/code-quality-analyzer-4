from typing import List
from collections import deque

class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        blocked_set = set(map(tuple, blocked))
        source_tuple = tuple(source)
        target_tuple = tuple(target)
        
        if source_tuple in blocked_set or target_tuple in blocked_set:
            return False
        
        if not blocked:
            return True
        
        m = len(blocked)
        