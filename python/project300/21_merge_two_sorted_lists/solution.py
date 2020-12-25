# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        a = l1
        b = l2
        c = ListNode()
        cp = c

        while a != None or b != None:
            if b == None or a != None and a.val <= b.val:
                cp.val = a.val
                a = a.next

            elif a == None or b != None and b.val <= a.val:
                cp.val = b.val
                b = b.next

            if a != None or b != None:
                cp.next = ListNode()
                cp = cp.next

        return c


s = Solution()
t1 = ListNode(1, ListNode(2, ListNode(4)))
t2 = ListNode(1, ListNode(3, ListNode(4)))
print(s.mergeTwoLists(t1, t2))