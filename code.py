import re

class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        if not s:
            return False
        # Regular expression pattern to match valid numbers
        pattern = r'^[+-]?((\d+\.?\d*)|(\.\d+))([eE][+-]?\d+)?$'
        return re.fullmatch(pattern, s) is not None