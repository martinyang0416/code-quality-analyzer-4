def numberOfSubarrays(nums, k):
    def at_most(k):
        count_odds = 0
        left = 0
        res = 0
        for right in range(len(nums)):
            if nums[right] % 2 == 1:
                count_odds += 1
            while count_odds > k:
                if nums[left] % 2 == 1:
                    count_odds -= 1
                left += 1
            res += right - left + 1
        return res
    
    return at_most(k) - at_most(k - 1)