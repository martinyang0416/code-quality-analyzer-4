names = ["Alfie", "Balthazar", "Cedric", "Duncan", "Evan"]

n = int(input())

if n <= 5:
    print(names[n-1])
else:
    m = 0
    while 5 * (2 ** (m + 1) - 1) < n:
        m += 1
    rem = n - 5 * (2 ** m - 1)
    per_wizard = 2 ** m
    wizard_index = (rem - 1) // per_wizard
    print(names[wizard_index])