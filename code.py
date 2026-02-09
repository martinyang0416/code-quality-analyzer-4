def maxTeams(a,b):
    ans=min((a+b)//3,min(a,b))
    return ans

inputArray=input().strip().split()
a=int(inputArray[0])
b=int(inputArray[1])
print(maxTeams(a,b))