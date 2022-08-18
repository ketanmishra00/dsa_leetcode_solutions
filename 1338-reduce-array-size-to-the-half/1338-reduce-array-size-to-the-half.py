from collections import Counter
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        d=Counter(arr)
        l=len(arr) # temparay variable to store  len of arr
        val=sorted(d.values())
        c=0 # counter to get length of a result set
        for i in range(len(val)-1,-1,-1):  # reverse traversal over sorted val list.
            l=l-val[i]
            c+=1
            if l<=len(arr)//2:
                break
        return c