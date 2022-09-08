class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        li_even=[]
        li_odd=[]
        for i in range(len(nums)):
            if nums[i]%2==0:
                li_even.append(nums[i])
            else:
                li_odd.append(nums[i])
        li_even.sort()
        li_odd.sort()
        return li_even+li_odd
        