class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        t=len(ransomNote)
        while (t!=0):
            for i in range(t):
                if ransomNote[i] in magazine:
                    indexs=magazine.index(ransomNote[i])
                    t-=1 
                    magazine=magazine[:indexs]+magazine[indexs+1:]
                elif ransomNote[i] not in magazine:
                    return False
        return True