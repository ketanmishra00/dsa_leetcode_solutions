class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
       # return nums1
        n=len(nums1)
        t=int((n)/2)
        if n%2!=0:
            m=float(nums1[t])
            return m
        
        m=(nums1[t] + nums1[t-1])/2
        return m
        