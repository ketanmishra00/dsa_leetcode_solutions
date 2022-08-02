class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        li=[]
        n=1
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                li.append(matrix[i][j])
                n+=1
        li.sort()        
        m=n-k
        return li[-m]
        