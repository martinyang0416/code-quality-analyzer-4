import sys

def main():
    sys.setrecursionlimit(1 << 25)
    def generate_all_pairings():
        elements = [1, 2, 3, 4, 5, 6]
        def helper(elems):
            if not elems:
                yield []
                return
            first = elems[0]
            for i in range(1, len(elems)):
                pair = (first, elems[i])
                remaining = elems[1:i] + elems[i+1:]
                for sub in helper(remaining):
                    yield [pair] + sub
        return lis