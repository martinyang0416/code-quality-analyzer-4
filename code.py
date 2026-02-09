from collections import deque
from typing import List

class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        available_boxes = set(initialBoxes)
        available_keys = set()
        processed = set()
        queue = deque()
        
        for box in initialBoxes:
            if status[box] == 1 or box in available_keys:
                queue.append(box)
        
        