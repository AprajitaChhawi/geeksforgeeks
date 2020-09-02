from array import *
def moore(a):
    maj=0
    count=1
    for i in range(len(a)):
        if(a[maj]==a[i]):
            count+=1
        else:
            count-=1
        if(count==0):
            maj=i
            count=1
    return a[maj]
t=int(input())
while t:
    t=t-1
    n=int(input())
    arr=[int(x) for x in input().split()]
    l=moore(arr)
    c=arr.count(l)
    if(l>len(arr)/2):
        print(l)
    else:
        print(-1)
