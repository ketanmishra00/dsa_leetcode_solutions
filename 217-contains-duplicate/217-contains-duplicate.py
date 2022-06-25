class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        lp=0
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                lp=1
        if lp==0:
            return False
        else:
            return True
        