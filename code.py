import decimal
import sys

def main():
    input = sys.stdin.read().split()
    t = int(input[0])
    idx = 1
    for _ in range(t):
        n = int(input[idx])
        k = int(input[idx+1])
        idx += 2
        
        # Compute last k digits
        mod = 10 ** k
        last_part = pow(n, n, mod)
        last = f"{last_part:0{k}d}"
        
        # Compute first k digits
        with decimal.localcontext() as ctx:
            ctx.prec = 50
            dn = decimal.Decimal(n)
          