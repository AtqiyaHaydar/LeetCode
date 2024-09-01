# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        remain = 0

        while l1 is not None or l2 is not None:    
            val1 = l1.val if l1 is not None else 0
            val2 = l2.val if l2 is not None else 0

            digit = val1 + val2 + remain
            
            remain = digit // 10
            digit = digit % 10
            
            current.next = ListNode(digit)
            current = current.next

            if l1 is not None: 
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
        
        if remain > 0:
            current.next = ListNode(remain)
        
        return dummy.next