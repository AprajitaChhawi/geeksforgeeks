t=int(input())
while t:
    t=t-1
    n=int(input())
    l=list(map(int,input().split()))
    temp=l[n-1]
    l1=l[0:n-1]
    l1.insert(0,temp)
    for i in l1:
        print(i,end=" ")
    print()
