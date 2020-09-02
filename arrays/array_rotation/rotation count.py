from array import *
try:
    t=int(input())
    while t:
        t=t-1
        n=int(input())
        arr=[int(x) for x in input().split()]
        for i in range(n):
            if(arr[i]>(arr[(i+1)%n])):
                print((i+1)%n)
except Exception:
    pass;
