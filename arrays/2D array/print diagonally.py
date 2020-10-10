try:
    t=int(input())
    while t:
        t=t-1
        n=int(input())
        l=[[]]
        for i in range(n):
            for j in range(n):
                l[i][j]=int(input().split())
        print(l)
except Exception:
    pass;
