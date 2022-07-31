class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        n=len(nums1)
        t=int((n)/2)
        if n%2!=0:
            return (nums1[t])
        return (nums1[t] + nums1[t-1])/2
        
        