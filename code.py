import bisect

def findLengthOfShortestSubarray(arr):
    n = len(arr)
    if n <= 1:
        return 0
    
    # Find the end of the longest non-decreasing prefix
    left_end = 0
    for i in range(1, n):
        if arr[i] >= arr[i-1]:
            left_end = i
        else:
            break
    if left_end == n - 1:
        return 0
    
    # Find the start of the longest non-decreasing suffix
    right_start = n - 1
    for i in range(n-2, -1, -1):
        if arr[i] <= arr[i+1]:
           