try:
    t=int(input())
    while t:
        t=t-1
        x,y=map(int,input().split())
        n=int(input())
        l=list(map(int,input().split()))
        sumx=sum(l[0::2])
        sumy=sum(l[1::2])
        print(x-sumx,y-sumy)
except Exception:
    pass;
