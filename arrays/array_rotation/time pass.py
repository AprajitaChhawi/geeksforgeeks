try:
    t=int(input())
    while t:
        t=t-1
        n,d=map(int,input().split())
        l=list(map(int,input().split()))
        b=[]
        if(d>n):
            d=d%n
        for i in range(n):
            b.append(l[(i+d)%n])
            
        for i in b:
            print(i,end=" ")
        print()
except Exception:
    pass;
