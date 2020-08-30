def search(l1,lower,higher,key1):
    if higher<lower:
        return -1
    mid=int((lower+higher)/2)
    if(l1[mid]==key1):
        return mid
    if(l1[lower]<=l1[mid]):
        if(key1>=l1[lower] and  key1<=l1[mid]):
            return search(l1,lower,mid-1,key1)
        return search(l1,mid+1,higher,key1)
    else:
        if(key1>=l1[mid] and key1<=l1[higher]):
            return search(l1,mid+1,higher,key1)
        return search(l1,lower,mid-1,key1)
t=int(input())
while t:
    t=t-1
    n=int(input())
    l=list(map(int,input().split()))
    k=int(input())
    i=search(l,0,n-1,k)
    print(i)
    
