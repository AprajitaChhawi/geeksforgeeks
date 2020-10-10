def rotate(matrix):
    temp=0
    for i in range(N):
        for j in range(i+1,N):
            matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
    for i in range(N):
        j=0
        k=N-1
        while j<k:
            matrix[j][i],matrix[k][i]=matrix[k][i],matrix[j][i]
            j=j+1
            k=k-1
t = int(input())
for _ in range(t):
    N=int(input())
    arr=[int(x) for x in input().split()]
    matrix=[]
    for i in range(0,N*N,N):
        matrix.append(arr[i:i+N])
    print(matrix)
    rotate(matrix)
    for i in range(N):
        for j in range(N):
            print(matrix[i][j], end=" ")
        print() 
