class Solution:
    def repeatedCharacter(self, s: str) -> str:
        li=[]
        for i in range(len(s)):
            if s[i] in li:
                return s[i]
            else:
                li.append(s[i])
        