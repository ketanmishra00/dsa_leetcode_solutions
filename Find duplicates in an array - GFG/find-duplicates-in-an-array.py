from collections import Counter
class Solution:
    
    def duplicates(self, arr, n): 
    	# code here
    	repeated = []
    	s = set()
        temp = set()
         
        for i in arr:
            if i in s:
                temp.add(i)
            else:
                s.add(i)
        temp = sorted(list(temp))
        if len(temp) == 0:
            return [-1]
        else:
            return temp
    	
    	            
    	
    	
    	
    	
    	
    	
    	
    	
    	
    	
    	'''repeated = []
    	for i in range(n):
    	    k = i+1
    	    for j in range(k,n):
    	        if arr[i] == arr[j] and arr[i] not in repeated:
                    repeated.append(x[i])
    	if len(repeated) > 0:
    	    return repeated
    	else:
    	    return -1'''
    	
            

#{ 
#  Driver Code Starts
if(__name__=='__main__'):
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        res = Solution().duplicates(arr, n)
        for i in res:
            print(i,end=" ")
        print()



# } Driver Code Ends