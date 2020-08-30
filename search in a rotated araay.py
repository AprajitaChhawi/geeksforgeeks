t=int(input())
while t:
    t=t-1
    n=int(input())
    l=list(map(int,input().split()))
    key=int(input())
    if(key in l):
        print(l.index(key))
    else:
        print(-1)
    
