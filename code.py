def getMaxRepetitions(s1, n1, s2, n2):
    len_s2 = len(s2)
    if len_s2 == 0:
        return 0
    
    # Precompute transitions for each starting position in s2
    transition = {}
    for p_start in range(len_s2):
        current_p = p_start
        count = 0
        for c in s1:
            if c == s2[current_p]:
                current_p += 1
                if current_p == len_s2:
                    count += 1
                    current_p = 0
        transition[p_start] = (count, curren