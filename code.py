def is_sorted(arr, inc):
    for i in range(len(arr)-1):
        if inc:
            if arr[i] > arr[i+1]:
                return False
        else:
            if arr[i] < arr[i+1]:
                return False
    return True

n = int(input())
a = list(map(int, input().split()))

sorted_inc = is_sorted(a, True)
sorted_dec = is_sorted(a, False)

if sorted_inc or sorted_dec:
    all_same = True
    for num in a[1:]:
        if num != a[0]:
            all_same = False
            break
    if a