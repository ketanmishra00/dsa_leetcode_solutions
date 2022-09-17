class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        i=0
        if n==1:
            return [nums]
        permutation=[]
        while i<n:
        
        
            nums[0],nums[i]=nums[i],nums[0]
            for p in self.permute(nums[1:]):
                p.append(nums[0])
                permutation.append(p)
            i+=1
        return permutation