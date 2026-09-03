# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Edge case 
        if not head: 
            return None 

        prev = None 
        cur = head 

        while cur is not None: 
            # Copy the next value first 
            t1 = cur.next 
        
            # Adjust the pointer backwards 
            cur.next = prev 
            
            # Increment the pointers 
            prev = cur 
            cur = t1
        
        return prev
