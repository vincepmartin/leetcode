# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None:
            return False

        p1 = head
        p2 = p1

        if p2.next == None:
            return False
        else:
            p2 = p2.next

        while p1 != None and p2 != None:
            if p1.val == p2.val:
                return True
            
            else:
                p1 = p1.next
                p2 = p2.next

                # We incremented by 1, but we need to move p2 forward 2 times.
                if p2 != None:
                    p2 = p2.next

        return False