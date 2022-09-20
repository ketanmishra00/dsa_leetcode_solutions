class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        n=0
        for i in num:
            n=n*10 + i
        n=n+k
        n=str(n)
        li=[]
        for i in n:
            li.append(int(i))
        return li
        