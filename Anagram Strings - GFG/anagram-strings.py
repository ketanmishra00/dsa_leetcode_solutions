#User function Template for python3
class Solution:
    def areAnagram(ob, S1, S2):
        # code here 
        n1=len(S1)
        n2=len(S2)
        if (n1!=n2):
            return 0
        s=sorted(S1)
        t=sorted(S2)
        for i in range(0, n1):
            if (s[i]!=t[i]):
                return 0
        return 1

#{ 
#  Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        S1 = input()
        S2 = input()
        
        ob = Solution()
        print(ob.areAnagram(S1,S2))
# } Driver Code Ends