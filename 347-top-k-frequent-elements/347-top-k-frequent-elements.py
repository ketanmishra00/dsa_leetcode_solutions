class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        
        for num in nums:
            d[num] = d.get(num, 0) + 1
        
        return sorted(d, key=d.get, reverse=True)[:k]
                
        