class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l=len(nums1)
        m=len(nums2)
        li=[]
        
        if l>m:
            for i in range(m):
                if nums2[i]  in nums1:
                    if nums2[i] not in li:
                        li.append(nums2[i])
        else:
            for i in range(l):
                if nums1[i]  in nums2:
                    if nums1[i] not in li:
                        li.append(nums1[i])
                        
        return li
                    
        