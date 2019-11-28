from typing import List
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return None

        if head.next != None:
            # Create temp as a copy of head and then behead it...
            newHead = self.reverseList(head.next)

            # go to end of new head and attach our new value.
            newHeadPointer = newHead
            while newHeadPointer.next != None:
                newHeadPointer = newHeadPointer.next
            newHeadPointer.next = ListNode(head.val)

            return newHead 
        else:
            return head

def printNode(head):
    p = head

    while p != None:
        print(f'{p.val}', end = ' ')
        p = p.next

    print()

s = Solution()
t1 = ListNode(1)
t1.next = ListNode(2)
t1.next.next = ListNode(3)
t1.next.next.next = ListNode(4)
t1.next.next.next.next = ListNode(5)
print('Before')
printNode(t1)
print('After')
printNode(s.reverseList(t1))