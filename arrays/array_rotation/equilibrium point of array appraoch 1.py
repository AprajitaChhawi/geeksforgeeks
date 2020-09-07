def mid(l,mi):
    if mi not in visited:
        visited.append(mi)
        if(sum(l[:mi])==sum(l[mi+1:])):
            return mi
        elif(mi==0 or mi==len(l)):
            return -1
        elif(sum(l[:mi])<sum(l[mi+1:])):
            return mid(l,mi+1)
        elif(sum(l[:mi])>sum(l[mi+1:])):
            return mid(l,mi-1)
    else:
        return -1
t=int(input())
while t:
    visited=[]
    t=t-1
    n=int(input())
    l1=list(map(int,input().split()))
    le=len(l1)
    if(n==1):
        print(1)
    else:
        k=mid(l1,int(len(l1)/2))
        if(k==-1):
            print(k)
        else:
            print(k+1)
            
            
            
            
            
            
            
            
