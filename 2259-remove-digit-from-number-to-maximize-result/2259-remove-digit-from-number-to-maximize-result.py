class Solution:
    def removeDigit(self, n: str, d: str) -> str:
        maxi=-10000
        for i in range(len(n)):
            if n[i]==d:
                maxi=max(maxi,int(n[:i]+n[i+1:])) #finding the maximum value among the remaining values
            
        return str(maxi)
        