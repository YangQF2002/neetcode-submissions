# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 0 1 2 3 


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        arr = []
        length = 0

        curr = head 
        while curr is not None:  
            arr.append(curr)
            length += 1
            curr = curr.next 

        low = 0 
        high = length - 1 
        turn = "low"
        
        curr = None 

        while low <= high: 
            index = low if turn == "low" else high

            if curr is None: 
                curr = arr[index] 
            else:
                curr.next = arr[index]
                curr = curr.next 

            if turn == "low": 
                low += 1
                turn = "high"
            else: 
                high -= 1 
                turn = "low"
                
        if curr: 
            curr.next = None 



    