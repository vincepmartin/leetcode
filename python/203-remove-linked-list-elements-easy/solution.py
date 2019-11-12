# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        a = head
        b = head

        # Head.
        if a.val == val:
            a.next = a.next.next
            return head

        if b.next != None:
            b = b.next

        while b != None:
            if b.val == val:
                a.next = b.next
                return head

            else:
                a = a.next
                b = b.next

        return head

s = Solution()
t1 = ListNode(1)
t1.next = ListNode(2)
t1.next.next = ListNode(3)
t1.next.next.next = ListNode(4)
t1.next.next.next.next = ListNode(5)
result = s.removeElements(t1, 5)
print(result)