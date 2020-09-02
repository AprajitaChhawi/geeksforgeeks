from array import *
t=int(input())
while t:
    t=t-1
    n=int(input())
    l=list(map(int,input().split()))
    for i in range(len(l)-1):
        temp=l[i]
        l1=l[i+1:]
        if(temp>=max(l1)):
            print(temp,end=" ")
    print(l[len(l)-1])
            
