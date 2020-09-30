try:
    t=int(input())
    while t:
        t=t-1
        l=[2,3,5,7]
        l1=[]
        n=int(input())
        while(n>0):
            temp=n%4
            if(temp==0):
                l1.append(7)
            else:
                l1.append(l[temp-1])
            n=int(n/4)
        l1.reverse()
        for i in l1:
            print(i,end="")
except Exception:
    pass;
