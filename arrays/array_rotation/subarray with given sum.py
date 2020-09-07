try:
    t=int(input())
    while t:
        t=t-1
        n,s=map(int,input().split())
        l=list(map(int,input().split()))
        su=0
        c=0
        for i in range(n):
            su=su+l[i]
            if(su>s):
                while(su>s):
                    su=su-l[c]
                    c=c+1
            if(su==s):
                print(c+1,i+1)
                break
            if(i==n and su!=s):
                print(-1)
except Exception:
    pass;
