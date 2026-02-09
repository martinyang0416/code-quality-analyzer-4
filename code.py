def main():
    import sys
    input = sys.stdin.read().split()
    n = int(input[0])
    result = []
    for i in range(n):
        a, b, c, d, e = map(int, input[1 + i*5 : 1 + i*5 +5])
        # Convert each number to 2-bit binary, padded to two characters
        bits_a = format(a, '02b')
        bits_b = format(b, '02b')
        bits_c = format(c, '02b')
        bits_d = format(d, '02b')
        bits_e = format(e, '02b')
        # Concatenate the bits
        total_bits = bits_a + bits_b + b