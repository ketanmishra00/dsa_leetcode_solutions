class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        if target not in nums:
            return [-1,-1]
        i=nums.index(target)
        high=i
        for j in range(i+1,len(nums)):
            if nums[j]==target:
                high+=1
        return[i,high]
                
            
        