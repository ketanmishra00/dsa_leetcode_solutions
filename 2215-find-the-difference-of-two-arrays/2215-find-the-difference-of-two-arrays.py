class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        li1=[]
        li2=[]
        for i in range(len(nums1)):
            if nums1[i] not in nums2 and nums1[i] not in li1:
                li1.append(nums1[i])
        for i in range(len(nums2)):
            if nums2[i] not in nums1 and nums2[i] not in li2:
                li2.append(nums2[i])
        li=[li1,li2]
        return li
        
        