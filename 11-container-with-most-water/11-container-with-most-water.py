class Solution:
    def maxArea(self, height: List[int]) -> int:
        maximum=0
        j,k= 0, len(height)-1
        i=0
        while(j<k):
            
            m=min(height[j],height[k])
            
            if m*(k-j)>maximum:
                maximum=m*(k-j)
            
            if height[j]<height[k]:
                j+=1
            else:
                k-=1
        return maximum