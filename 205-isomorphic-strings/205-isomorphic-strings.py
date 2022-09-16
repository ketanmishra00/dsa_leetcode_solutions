class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        li=[]
        li1=[]
        for i in s:
            li.append(s.index(i))
        for i in t:
            li1.append(t.index(i))
        if li == li1:
            return True
        return False
        