class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        #index = vowels.index('e')
        return nums.index(max(nums))
        