#User function Template for python3

class Solution:
    def LastIndex(self, s, p):
        # code here
        n=len(s)
        for i in range(n-1, 0-1, -1):
            if p==s[i]:
                return i
        return -1
            
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        s = input().strip()
        p = input().strip()[0]
        
        ob=Solution()
        print(ob.LastIndex(s, p))
# } Driver Code Ends