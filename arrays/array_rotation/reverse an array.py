t=int(input())
while t:
    t=t-1
    n=int(input())
    l=list(map(int,input().split()))
    l.reverse()
    for i in l:
        print(i,end=" ")
    print()
