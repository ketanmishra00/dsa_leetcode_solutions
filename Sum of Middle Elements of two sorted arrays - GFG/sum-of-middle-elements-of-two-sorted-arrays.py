#User function Template for python3

class Solution:
	def findMidSum(self, ar1, ar2, n): 
		# code here
		arres = ar1 + ar2
		arres.sort()
		l=0
		h=n*2 - 1
		mid = (l + h)//2
		res = arres[mid] + arres[mid + 1]
		return res

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__": 		
    tc=int(input())
    while tc > 0:
        n=int(input())
        ar1=list(map(int, input().strip().split()))
        ar2=list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findMidSum(ar1, ar2, n)
        print(ans)
        tc=tc-1

# } Driver Code Ends