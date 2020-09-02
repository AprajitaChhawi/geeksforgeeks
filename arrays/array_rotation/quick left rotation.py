try:
    t=int(input())
    while t:
        t=t-1
        n,r=map(int,input().split())
        l=list(map(int,input().split()))
        r1=r%len(l)
        for i in range(r1,len(l)):
            print(l[i],end=" ")
        for i in range(0,r1):
            print(l[i],end=" ")
        print()
except Exception:
    pass;
