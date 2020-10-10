try:
    t=int(input())
    while t:
        t=t-1
        n=int(input())
        matrix=[]
        for i in range(n):
            matrix.append([int(j)for j in input().split()])
        print(matrix)
        l1=[]
        l2=[]
        for i in range(n):
            l1.append(matrix[i][i])
            l2.append(matrix[i][n-i-1])
        print(l1)
        print(l2)
except Exception:
    pass;
                    
                
