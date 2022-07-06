class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        li = len(nums)
        for i in range(li):
             nums[i] = nums[i] * nums[i]
        nums.sort()
        return nums
        