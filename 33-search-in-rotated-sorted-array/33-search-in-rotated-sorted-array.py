class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target in nums:
            res = nums.index(target)
            return res
        return -1
            
        