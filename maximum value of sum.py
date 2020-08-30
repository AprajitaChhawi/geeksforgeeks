def maxsum(l1):
    s=sum(l1)
    n=len(l)
    maw=0
    for i in range(0,len(l)):
        maw=maw+i*l[i]
    maximum=maw
    for j in range(1,len(l)):
        value=maw+s-l1[n-j]*n
        maw=value
        if(value>maximum):
            maximum=value
    return maximum
l=list(map(int,input().split()))
m=maxsum(l)
print(m)

    
    
