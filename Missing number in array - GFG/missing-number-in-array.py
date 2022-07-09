#User function Template for python3


class Solution:
    def MissingNumber(self,array,n):
        # code here
        x = len(array)
        total = (x + 1)*(x + 2)/2
        sum_of_array = sum(array)
        return int(total - sum_of_array)
        
#{ 
#  Driver Code Starts
#Initial Template for Python 3




t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    s=Solution().MissingNumber(a,n)
    print(s)
# } Driver Code Ends