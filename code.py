def compute_max(even, odd, start_even):
    e_ptr = 0
    o_ptr = 0
    sum_total = 0
    current_parity = None
    
    if start_even:
        if e_ptr >= len(even):
            return 0
        sum_total += even[e_ptr]
        e_ptr += 1
        current_parity = 0
    else:
        if o_ptr >= len(odd):
            return 0
        sum_total += odd[o_ptr]
        o_ptr += 1
        current_parity = 1
    
    while True:
        if current_parity == 0:
            # Next needs to be odd
      