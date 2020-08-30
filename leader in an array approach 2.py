t=int(input())
while t:
    t=t-1
    n=int(input())
    maxx=-1
    l2=[]
    l=list(map(int,input().split()))
    for i in range(len(l)-1,-1,-1):
        if(l[i]>=maxx):
            maxx=l[i]
            l2.append(l[i])
    l2.sort(reverse=True)
    for i in l2:
        print(i,end=" ")
    print()
        
            
        
