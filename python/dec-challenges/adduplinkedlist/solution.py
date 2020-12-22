# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        p = head
        tempNum = []

        while p != None:
            tempNum.append(str(p.val))
            p = p.next

        newNum = list(str(int(''.join(tempNum)) + 1))
        
        p = head

        for i in range(len(newNum)):
            # Not at the last Node.
            if i != len(newNum) - 1:
                p.val = int(newNum[i])
                p.next = ListNode()
                p = p.next
            # At the last Node.
            else:
                p.val = int(newNum[i])

        return head


s = Solution()
t1 = ListNode(1)
t1.next = ListNode(2)
t1.next.next = ListNode(3)

print(s.plusOne(t1))