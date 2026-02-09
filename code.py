A_str = "What are you doing while sending "  # length 32
B_str = " Are you busy? Will you send "      # length 29
f0_str = "What are you doing at the end of the world? Are you busy? Will you save us?"

def solve():
    import sys
    input = sys.stdin.read().split()
    q = int(input[0])
    idx = 1
    output = []
    for _ in range(q):
        n = int(input[idx])
        k = int(input[idx+1])
        idx +=2

        if n > 60:
            # Proceed since L_n is way larger than k
            c