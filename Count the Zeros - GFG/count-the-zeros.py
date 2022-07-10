#User function Template for python3

class Solution:
    def countZeroes(self, arr, n):
        # code here
        t=0
        for i in range(len(arr)):
            if arr[i] == 0:
                t+=1
        return t
            

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.countZeroes(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends