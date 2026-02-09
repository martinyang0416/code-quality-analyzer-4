def findMedianSortedArrays(nums1, nums2):
    # Ensure nums1 is the smaller array to minimize binary search steps
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    m, n = len(nums1), len(nums2)
    low, high = 0, m
    total = m + n
    half = (total + 1) // 2  # Correctly compute the half for partitioning
    
    while low <= high:
        i = (low + high) // 2  # Partition point in nums1
        j = half - i           # Corresponding partition point in nums2
        
   