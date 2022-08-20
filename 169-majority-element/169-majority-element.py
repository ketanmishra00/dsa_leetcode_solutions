class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        from collections import Counter
        hashmap = Counter(nums)  # counts occurrences of elements of nums
        return max(hashmap, key=hashmap.get) 
        