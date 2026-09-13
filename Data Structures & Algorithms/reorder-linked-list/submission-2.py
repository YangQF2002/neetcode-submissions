# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# O(1) space 


# []
# slow = fast = None 

# [1]

# slow = fast = 1 
# prev = 1 
# 1 -> None | 1 -> None



class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head and not head.next: 
            return 

        slow = fast = head 

        # Once we identified middle, we want to cut the prev -> middle connection 
        prev = None 
        while slow is not None and fast is not None and fast.next is not None: 
            prev = slow 
            slow = slow.next 
            fast = fast.next.next 

            # Pre-emptive check if we have slow == middle 
            # Then, cut the connection 
            if fast is None or fast.next is None: 
                prev.next = None 

        # At the end, the slow == middle 
        # Now, reverse the (middle - end) half 
        prev = None 
        curr = slow 

        while curr is not None: 
            temp = curr.next 
            curr.next = prev

            prev = curr
            curr = temp 
        
        # Now, prev == end is the new head of the reversed half 
        # Now, do an alternating merge, starting from (start - middle) half's turn 
        is_lower_turn = True 

        lower_p = head 
        upper_p = prev 
        curr = None 
        
        while lower_p is not None and upper_p is not None: 
            if is_lower_turn: 
                if curr is None: 
                    curr = lower_p 
                else: 
                    curr.next = lower_p 
                    curr = curr.next 

                lower_p = lower_p.next 
            else:     
                if curr is None: 
                    curr = upper_p 
                else: 
                    curr.next = upper_p 
                    curr = curr.next 

                upper_p = upper_p.next

            is_lower_turn = not is_lower_turn

        # Merge in the remaining 
        if lower_p is not None: 
            if curr is None: 
                curr = lower_p 
            else:
                curr.next = lower_p 
                curr = curr.next

            lower_p = lower_p.next
            
        if upper_p is not None: 
            if curr is None: 
                curr = upper_p
            else:
                curr.next = upper_p
                curr = curr.next

            upper_p = upper_p.next


        


        
        
        