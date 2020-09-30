from math import ceil
try:
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    s=0
    for i in range(n):
        temp=ceil(int(l[i]/k))+1
        s=s+temp
    print(s)
except Exception:
    pass;
        
        
