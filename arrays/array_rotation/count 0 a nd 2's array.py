try:
    t=int(input())
    while t:
        t=t-1
        n=int(input())
        l=list(map(int,input().split()))
        c=l.count(0)
        print('0 '*c,end="")
        c1=l.count(1)
        print('1 '*c1,end="")
        c3=l.count(2)
        print('2 '*c3,end="")
        print()
except Exception:
    pass;
