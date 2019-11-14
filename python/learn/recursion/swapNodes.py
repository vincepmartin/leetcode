# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        return self.helper(head, True)

    def helper(self, curr, swap) -> ListNode:
        print(f'Processing: {curr.val}')

        if curr.next == None:
            return curr

        else:
            curr.next = self.helper(curr.next, not swap)
            if swap:
                temp = curr.next
                curr.next = curr.next.next
                temp.next = curr
                return temp 
            return curr

s = Solution()
t2 = ListNode(None)
t1 = ListNode(1)
t1.next = ListNode(2)
t1.next.next = ListNode(3)
t1.next.next.next = ListNode(4)

nachos = s.swapPairs(t2)
print(nachos)
