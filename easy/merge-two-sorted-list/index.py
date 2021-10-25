from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 and not l2:
            return None

        if not l2: 
            return l1

        if not l1:
            return l2
        
        dummy = ListNode() # (0, None)
        prev = dummy

        while l1 and l2:
            if l1.val < l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next

            prev = prev.next # proceed for replace
          
        if l1: 
            prev.next = l1

        if l2: 
            prev.next = l2

        return dummy.next