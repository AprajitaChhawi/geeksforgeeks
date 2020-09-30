def kadane(l,n):
    max1=0
    max2=0
    for i in l:
        max2=max2+i
        if(max1<max2):
            max1=max2
        if(max2<0):
            max2=0
    return max2
try:
    t=int(input())
    while t:
        t=t-1
        n=int(input())
        l=list(map(int,input().split()))
        if(max(l)<0):
            print(max(l))
        elif(min(l)>=0):
            print(sum(l))
        else:
            s=kadane(l,n)
            print(s)
except Exception:
    pass;
