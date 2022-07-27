if target not in nums:
return [-1,-1]
low=0
high=len(nums)-1
while(low<=high):
if nums[low]==nums[high]==target:
return[low,high]
if nums[low]<target:
low+=1
if nums[high]>target:
high+1
*                 Runtime: 98 ms, faster than 80.54% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.
Memory Usage: 15.4 MB, less than 93.21% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.