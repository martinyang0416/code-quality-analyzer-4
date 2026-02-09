import collections

def solve():
    N=int(input())
    A=list(map(int,input().split()))
    c=collections.Counter(A)
    max_count = sorted(c.values(), reverse=True)[0]
    max_key = [k for k in c.keys() if c[k] == max_count][0]
    pivot = A.index(max_key)
    ans=[]
    for i in range(pivot-1, -1, -1):
        if A[i]<max_key:
            ans.append([1,i+1,i+2])
        else:
            ans.append([2,i+1,i+2])
    #print(max_key,pivot)
    for i in range(pivot+1, N):
        if A[i]==max_key