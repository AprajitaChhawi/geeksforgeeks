try:
    t=int(input())
    while t:
        t=t-1
        n=int(input())
        l=list(map(int,input().split()))
        d={}
        for i in range(n):
            d[i+1]=l[i]
        for(key,value) in sorted(d.items(),key=lambda x:x[1]):
            print(key,end=" ")
        print()
except Exception:
    pass;
            
            
