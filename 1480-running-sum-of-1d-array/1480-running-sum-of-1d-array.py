class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        s=0
        li=[]
        for i in range(len(nums)):
            s=s + nums[i]
            li.append(s)
        return li            
            