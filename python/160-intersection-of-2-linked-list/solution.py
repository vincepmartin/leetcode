import time
import gc 

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def lengthOfList(self, head):
        length = 0
        p = head
        while p != None:
            length = length + 1 
            p = p.next
        return length

    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # Check for tom foolery
        if headA == None or headB == None:
            return None

        l = None
        lHead = None
        s = None

        # Match details.
        m = None
        mCount = 0

        if self.lengthOfList(headA) < self.lengthOfList(headB):
            s = headA
            l = headB
            lHead = headB
            
        else:
            s = headB
            l = headA
            lHead = headA
        
        while s != None:
            if s.val != l.val:
                m = None
                mCount = 0
                if l.next != None:
                    l = l.next
                else:
                    l = lHead
                    s = s.next

            elif s.val == l.val:
                if mCount == 0:
                    m = s
                mCount += 1

                s = s.next

                if l.next != None:
                    l = l.next
                else:
                    l = lHead

        if not m:
            return None
        else:
            return m


s = Solution()

# 4 1 8 4 5 vs 5 0 1 8 4 5
testa1 = ListNode(4)
testa1.next = ListNode(1)
testa1.next.next = ListNode(8)
testa1.next.next.next = ListNode(4)
testa1.next.next.next.next = ListNode(5)

testb1 = ListNode(5)
testb1.next = ListNode(0)
testb1.next.next = ListNode(1)
testb1.next.next.next = ListNode(8)
testb1.next.next.next.next = ListNode(4)
testb1.next.next.next.next.next = ListNode(5)
print(s.getIntersectionNode(testa1, testb1).val)

testa2 = ListNode(2)
testa2.next = ListNode(6)
testa2.next.next = ListNode(4)

testb2 = ListNode(1)
testb2.next = ListNode(5)
print(s.getIntersectionNode(testa2, testb2))
