from collections import defaultdict

def totalFruit(tree):
    count = defaultdict(int)
    left = 0
    max_fruits = 0
    for right in range(len(tree)):
        fruit = tree[right]
        count[fruit] += 1
        while len(count) > 2:
            left_fruit = tree[left]
            count[left_fruit] -= 1
            if count[left_fruit] == 0:
                del count[left_fruit]
            left += 1
        max_fruits = max(max_fruits, right - left + 1)
    return max_fruits