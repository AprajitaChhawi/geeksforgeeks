#User function Template for python3
class Solution:
    def onesComplement(self,S,N):
        s=""
        for i in S:
            if(i=='0'):
                s+='1'
            elif(i=='1'):
                s+='0'
        return s
        
        # code here



#{ 
#  Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        S = input()
        ob = Solution()
        print(ob.onesComplement(S,N))
# } Driver Code Ends
