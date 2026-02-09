def main():
    import sys

    prefix_str = "What are you doing while sending "
    middle_str = " Are you busy? Will you send "
    f0_str = "What are you doing at the end of the world? Are you busy? Will you save us?"

    def compute_L(n):
        if n == 0:
            return 75
        L = 75
        for i in range(1, n + 1):
            L = 2 * L + 67
        return L

    def get_char(n, k):
        current_n = n
        current_k = k
        while True:
            if current_n == 0:
  