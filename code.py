import bisect

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    idx = 0
    c = int(data[idx])
    idx +=1
    results = []
    for _ in range(c):
        n = int(data[idx])
        m = int(data[idx+1])
        T = int(data[idx+2])
        idx +=3
        p = list(map(int, data[idx:idx+n]))
        idx +=n
        
        p.sort()
        prefix = [0]
        current = 0
        for num in p:
            current += num
            prefix.append(current)
     