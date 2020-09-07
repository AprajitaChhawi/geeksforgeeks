try:
    t=int(input())
    while t:
        t=t-1
        n=int(input())
        s=((n+1)*n)/2
        l=list(map(int,input().split()))
        s1=sum(l)
        print(int(s-s1))
except Exception:
    pass;
