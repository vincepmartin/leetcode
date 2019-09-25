# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        if head is None:
            return head

        # Fast and slow pointers.
        ps = head
        pf = head
        
        while pf and pf.next:
            ps = ps.next
            pf = pf.next.next

        return ps
        
        