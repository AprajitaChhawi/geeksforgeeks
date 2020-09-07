try:
    t=int(input())
    while t:
        t=t-1
        n=int(input())
        l=list(map(int,input().split()))
        k=int(input())
        l1=sorted(l)
        print(l1[k-1])
except Exception:
    pass;
                
