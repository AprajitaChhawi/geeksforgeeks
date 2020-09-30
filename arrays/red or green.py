#User function Template for python3

class Solution:
    def RedOrGreen(self,N,S):
        rc=S.count('R')
        rg=S.count('G')
        return N-max(rc,rg)
        
        #code here



#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N=int(input())
        S=input()
        
        ob=Solution()
        print(ob.RedOrGreen(N,S))
# } Driver Code Ends
