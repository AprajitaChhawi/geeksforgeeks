try:
    t=int(input())
    while t:
        t=t-1
        n=int(input())
        matrix=[]
        for i in range(n):
            a=[]
            for j in range(n):
                a.append(int(input()))
            matrix.append(a)
        print(matrix)
        for k in range(n):
            j=k
            i=0
            while(j>=0):
                print(matrix[i][j],end=" ")
                j=j-1
                i=i+1
        for k in range(1,n+1):
            j=n-1
            i=k
            while(i<=n-1):
                print(matrix[i][j],end=" ")
                j=j-1
                i=i+1
except Exception:
    pass;
            
            
