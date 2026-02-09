def clumsy(N: int) -> int:
    if N == 0:
        return 0
    current_term = N
    terms = []
    current_sign = 1
    op_index = 0
    ops = ['*', '/', '+', '-']
    for i in range(N-1, 0, -1):
        op = ops[op_index % 4]
        if op in ('*', '/'):
            if op == '*':
                current_term *= i
            else:
                current_term = current_term // i
            op_index += 1
        else:
            terms.append(current_sign * current_term)
            current_sig