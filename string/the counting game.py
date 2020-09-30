import re
t=int(input())
while t:
    t=t-1
    s=input()
    if(len(s)==0):
        print(0)
    count=0
    for i in s:
        if(re.match("^[A-Z]$",i)):
            count=count+1
    print(count+1)
        
