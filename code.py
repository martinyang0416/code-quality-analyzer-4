n = int(input())

# Read set A
a_input = list(map(int, input().split()))
a = set(a_input[1:]) if a_input[0] > 0 else set()

# Read set B
b_input = list(map(int, input().split()))
b = set(b_input[1:]) if b_input[0] > 0 else set()

# Read set C
c_input = list(map(int, input().split()))
c = set(c_input[1:]) if c_input[0] > 0 else set()

# Compute required sets
set1 = c - a
set2 = b & c

# Calculate union and output the size
print(len(set1.union(set2)))