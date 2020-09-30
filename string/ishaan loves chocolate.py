try:
    t=int(input())
    while t:
        t=t-1
        n=int(input())
        l=list(map(int,input().split()))
        if(len(set(l))==1):
            print(l[0])
        else:
            print(min(l))
except Exception:
    pass;
