class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n=1
        nums=sorted(list(set(nums)))
        for i in nums:
            if(i>0 and n!=i):
                return n
            elif(i>0):
                n+=1
        return n