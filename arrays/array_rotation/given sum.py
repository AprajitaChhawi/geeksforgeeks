l=list(map(int,input().split()))
s=int(input())
flag=0
for i in l:
    if((s-i) in l):
        flag=1
        key=i
if(flag==0):
    print(-1)
else:
    w=l.index(s-key)
    print(key,l[w])
