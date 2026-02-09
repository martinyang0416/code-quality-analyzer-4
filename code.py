n = int(input())
typedefs = {}

for _ in range(n):
    parts = input().strip().split()
    if parts[0] == 'typedef':
        A, B = parts[1], parts[2]
        base_name = ''.join([c for c in A if c not in '*&'])
        modifiers = [c for c in A if c in '*&']
        num_stars = modifiers.count('*')
        num_amps = modifiers.count('&')
        
        if base_name == 'void':
            current_base, current_ptr = 'void', 0
        elif base_name == 'errtype':
            current_base, curre