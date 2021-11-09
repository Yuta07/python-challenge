from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        dummy = head
        x = head.next

        while x:
            if x.val == dummy.val:
                dummy.next = x.next
                x = x.next
            else:
                dummy = x
                x = x.next
                
        return head