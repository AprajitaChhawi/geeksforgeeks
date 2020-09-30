try:
    t=int(input())
    while t:
        t=t-1
        n=int(input())
        l=list(map(int,input().split()))
        left=[]
        right=[]
        left.append(l[0])
        for i in range(1,n):
            left.append(max(l[i],left[i-1]))
            print(left)
        right.insert(n-1,l[-1])
        for i in range(len(l)-2,-1,-1):
            right.append(max(l[i],right[i+1]))
            print(right)
        for i in range(0,len(l)):
            res=min(max(left[i],right[i]))-l[i]
            if(res>0):
                s=s+res
        print(s)
except Exception:
    pass;
            
            
            
            
            
