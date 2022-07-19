class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()

        final = []
        que = []

        for number in nums:
            if number in final:
                que.append(number)

            else:
                final.append(number)

        for number in que:
            final.remove(number)

        return final[0]
            
        