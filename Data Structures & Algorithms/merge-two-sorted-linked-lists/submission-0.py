# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution: 
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = None 
        cur = None 

        cur_l1 = list1
        cur_l2 = list2 
        while cur_l1 is not None and cur_l2 is not None: 
            l1_val = cur_l1.val
            l2_val = cur_l2.val 

            if l1_val <= l2_val: 
                if head is None: 
                    head = cur_l1 
                    cur = head 
                else: 
                    cur.next = cur_l1 
                    cur = cur.next 
                
                cur_l1 = cur_l1.next 
            else: 
                if head is None: 
                    head = cur_l2
                    cur = head 
                else: 
                    cur.next = cur_l2
                    cur = cur.next 

                cur_l2 = cur_l2.next 
        
        # Edge case: Continue exhausting the non-empty pointer 
        # Either one is non-empty or none is non-empty 
        non_empty_l = cur_l1 if cur_l1 is not None else cur_l2 
        while non_empty_l is not None: 
            if head is None: 
                head = non_empty_l 
                cur = head 
            else: 
                cur.next = non_empty_l 
                cur = cur.next 
            
            non_empty_l = non_empty_l.next

        return head 


        
        
        