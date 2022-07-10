class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        slow= head
        fast= head
        if head is None:
            return False
        
        else:
            while(slow is not None and fast is not None and fast.next is not None):
                slow = slow.next
                fast = fast.next.next
            
                if(slow==fast):
                    return True
        
        
        
        return False