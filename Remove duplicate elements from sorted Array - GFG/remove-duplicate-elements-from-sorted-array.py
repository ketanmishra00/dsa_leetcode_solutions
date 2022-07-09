#User function template for Python

class Solution:	
	def remove_duplicate(self, A, N):
		# code here
		
		for i in range(N-1,0,-1):
		    
	        if (A[i]==A[i-1]):
	            del A[i]
        l = len(A)
		
		return l
		        
		    

#{ 
#  Driver Code Starts
#Initial template for Python

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        N = int(input())
        A = list(map(int, input().strip().split()))
        ob = Solution()
        n = ob.remove_duplicate(A,N)
        for i in range(n):
            print(A[i], end=" ")
        print()


# } Driver Code Ends