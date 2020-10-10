def countZeros(A, N):
    count=0
    for i in range(N):
        k=N-1
        while(k>0 and A[k][i]==1):
            k=k-1
        count=count+(k+1)
    return count
            
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input().strip())
        arr = list(map(int, input().strip().split()))
        matrix = [[0 for i in range(n)]for j in range(n)]
        k=0
        for i in range(n):
            for j in range(n):
                matrix[i][j] = arr[k]
                k+=1
        print(countZeros(matrix, n))
