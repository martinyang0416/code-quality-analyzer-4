def nod(a,b):
    while a*b!=0:
        if a>b:
            a%=b
        else:
            b%=a
    return a+b
n,m=map(int,input().split())
l=[int(j) for j in input().split()]
p=[int(j) for j in input().split()]

nd=l[1]-l[0]
ans=-1
for i in range(2,n):

    nd=nod(nd,l[i]-l[i-1])
    
for i in range(m):
   
    if nd%p[i]==0:
        ans=i
        break
    
if ans==-1:
    print('NO')
else:
    print('YES')
    print(l[0],ans+1)
    

    
