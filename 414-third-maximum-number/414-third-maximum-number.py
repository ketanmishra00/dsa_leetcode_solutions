class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        li=[]
        for i in range(len(nums)):
            if nums[i] not in li:
                li.append(nums[i])
        li.sort()
        if len(li)>2:
            return li[len(li)-3]
        return li[-1]
        