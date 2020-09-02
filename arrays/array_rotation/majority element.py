from array import *
try:
    t=int(input())
    while t:
        n=int(input())
        flag=0
        arr=[int(x) for x in input().split()]
        arr.sort()
        mid=int(len(arr)/2)
        item=arr[mid]
        co=arr.count(item)
        if(co>mid):
            print(item)
        else:
            print(-1)
except Exception:
    pass;
