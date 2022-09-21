class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        #d = {}
        res = []
        sumE = 0
        for n in nums:
            if n%2==0:
                #d[i] = n
                sumE+=n
        
        for q in queries:
            i = q[1]
            v = q[0]
            if nums[i]%2==0:
                sumE-=nums[i]
                if (nums[i]+v)%2==0:
                    sumE+=(nums[i]+v)
            else:
                if (nums[i]+v)%2==0:
                    sumE+=(nums[i]+v)
            nums[i]+=v
            res.append(sumE)
        return res