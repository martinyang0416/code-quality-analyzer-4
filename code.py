class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        costs = [abs(ord(sc) - ord(tc)) for sc, tc in zip(s, t)]
        left = current_sum = max_len = 0
        for right in range(len(costs)):
            current_sum += costs[right]
            while current_sum > maxCost:
                current_sum -= costs[left]
                left += 1
            max_len = max(max_len, right - left + 1)
        return max_len