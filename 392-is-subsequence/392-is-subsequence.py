class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_index = 0
        count = 0
        
        if len(s)>0:
            for x in t:
                if s[s_index]==x:
                    count+=1
                    s_index+=1
                    if s_index==len(s):
                        break
        return count==len(s)
        