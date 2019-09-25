# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def bothAtEnd(self, p1, p2):
        if p1.next == p2.next and p1.next == None and p2.next == None:
            return True
        else:
            return False
        
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        
        # Check for idiotic inputs...
        if headA == None or headB == None:
            return None

        p1 = headA
        p2 = headB

        p1CurrentList = 'a'
        p2CurrentList = 'b'

        while True:
            if p1 == p2:
                print("We have a match! ", p1.val, " and ", p2.val)
                return p1

            print("No Match, increment...")
            p1, p1CurrentList = self.incrementOrLoop(p1, p1CurrentList, headA, headB)
            p2, p2CurrentList = self.incrementOrLoop(p2, p2CurrentList, headA, headB)

        print("In theory should be None") 
        return None 

s = Solution()

# 4 1 8 4 5 vs 5 0 1 8 4 5
print("Should be 8.")
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
sol = s.getIntersectionNode(testa1, testb1)
print(sol)

print("*****")
print("Should be none...")
testa2 = ListNode(2)
testa2.next = ListNode(6)
testa2.next.next = ListNode(4)
testb2 = ListNode(1)
testb2.next = ListNode(5)
sol = s.getIntersectionNode(testa2, testb2)
print sol
