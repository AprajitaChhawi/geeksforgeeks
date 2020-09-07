try:
    t=int(input())
    while t:
        t=t-1
        n=int(input())
        l=list(map(int,input().split()))
        if(n==1):
            print(1)
        else:
            leftsum=l[0]
            rightsum=sum(l)-l[0]-l[1]
            for i in range(1,n):
                if(leftsum==sum(l) or rightsum==0):
                    print(-1)
                if(leftsum==rightsum):
                    print(i+1)
                    break
                leftsum=leftsum+l[i]
                rightsum=rightsum-l[i+1]
except Exception:
    pass;
        
        
