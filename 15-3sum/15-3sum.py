class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        r = []
        n = 0
        while n < len(nums):
            t = -nums[n]
            
            i = n+1
            j = len(nums)-1
            
            while i < j:
                if nums[i] + nums[j] > t:
                    j -= 1
                elif nums[i] + nums[j] < t:
                    i += 1
                else:
                    r.append([-t,nums[i],nums[j]])
                    b = nums[j]
                    
                    while j >=0 and b == nums[j]:
                        j = j - 1
                        
            while n < len(nums) and -t == nums[n]:
                n = n+1
            # print(n)
        return r