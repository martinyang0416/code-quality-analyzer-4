def min_subarray(nums, p):
    total_sum = sum(nums)
    if total_sum % p == 0:
        return 0
    rem = total_sum % p
    prefix_mods = {0: -1}
    current_sum = 0
    min_len = float('inf')
    for i in range(len(nums)):
        current_sum += nums[i]
        current_mod = current_sum % p
        target_mod = (current_mod - rem) % p
        if target_mod in prefix_mods:
            candidate = i - prefix_mods[target_mod]
            if candidate < min_len:
                min_len = candidate