# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        curr = head
        prev = curr

        while curr:
            if curr.val == val:
                prev.next = curr.next
                curr = prev.next
            
            else:
                prev = curr

            if curr: 
                curr = curr.next
        
        return head

    def removeElementsFailsLeetCode(self, head: ListNode, val: int) -> ListNode:
        a = head
        b = head

        # Head.
        if a.val == val:
            head = a.next 
            return head

        # Jump B to next if it exists.
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
t1.next.next.next.next.next = ListNode(6)
result = s.removeElements(t1, 6)
print(result)