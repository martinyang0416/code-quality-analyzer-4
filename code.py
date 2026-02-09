'''
import math

def BearAndBigBrother():
    a, b = map(int, input().split(' '))
    year = 0
    while 1:
        if a > b:
            break
        else:
            a *= 3
            b *= 2
            year += 1
    print(year)
    return None

def Tram():
    n = int(input())
    p = [0]
    for i in range(1, n+1):
        a, b = map(int, input().split())
        tmp = p[i-1]
        tmp -= a
        tmp += b
        p.append(tmp)
    print(max(p))
    return None


def WrongSubtraction()