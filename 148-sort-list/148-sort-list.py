# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
	def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

		values = []

		curr = head

		while curr:
			values.append(curr.val)
			curr = curr.next

		values.sort()

		dummy = ListNode(0)
		head = dummy
		i =0
		while i < len(values):
			curr = ListNode(values[i])
			dummy.next = curr
			i+=1
			dummy = dummy.next

		return head.next
    
        