
class Solution:
    def minValueToBalance(self,a,n):
        k1=sum(a[:int((n)/2)])
        k2=sum(a[int(n/2):])
        print(k1)
        print(k2)
        if(k1<k2):
            return k2-k1
        else:
            return k1-k2



#{ 
#  Driver Code Starts
#Initial Template for Python 3





t=int(input())
for _ in range(0,t):
    n=int(input())
    a = list(map(int,input().split()))
    ob = Solution()
    ans=ob.minValueToBalance(a,n)
    print(ans)

# } Driver Code Ends
