class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        t=len(ransomNote)
        while (t!=0):
            for i in range(t):
                if ransomNote[i] in magazine:
                    #index = animals.index('dog')
                    indexs=magazine.index(ransomNote[i])
                    t-=1
                    #new_str = test_str[:2] +  test_str[3:]
                    
                    magazine=magazine[:indexs]+magazine[indexs+1:]
                elif ransomNote[i] not in magazine:
                    return False
        return True