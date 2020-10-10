gradefile=open("input.txt","r")
numexams=int(gradefile.readline())
numstudents=int(gradefile.readline())
s=0
examgrades=[[int(num) for num in line.split()]for line in gradefile]
for i in range(0,numexams):
    for j in range(0,numstudents):
        s=s+examgrades[i][j]
print(s/i)
print(examgrades)
gradefile.close()
