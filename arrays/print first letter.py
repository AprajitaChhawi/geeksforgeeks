#User function Template for python3
class Solution:
    def firstAlphabet(self,S):
        l=""
        for i in S.split(" "):
            l=l+i[0]
        return l;
                

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        S = input()
        ob = Solution()
        answer = ob.firstAlphabet(S)
        print(answer)
