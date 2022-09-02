class Solution:
    def intersection(self, nums):
        intersect = set(nums[0])
        for num in nums:
            intersect = intersect.intersection(num)
        return sorted(intersect)

            
            
            