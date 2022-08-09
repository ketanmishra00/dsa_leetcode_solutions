class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        prefix = []
        for i in range(len(nums)):
            prefix.append(sum(nums[:i+1]))
        for j in range(len(nums)):
            if sum(nums[j:]) == prefix[j]:
                return j
        return -1