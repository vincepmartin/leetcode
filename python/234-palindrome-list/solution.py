import math

# Definition for singly-linked list.
class ListNode(object):
   def __init__(self, x):
       self.val = x
       self.next = None

class Solution(object):
    cache = {} 

    def getVal(self, head, loc, max):
        p = head

        if head.next == None:
            return True

        for i in range(0,max + 1):
            # print("i: ", str(i), " with val: ", str(p.val))
            if i == loc:
                return p.val
            p = p.next

    def dynamicGetVal(self, head, loc, max):
        p = head

        if head.next == None:
            return True

        if loc in Solution.cache:
            return Solution.cache.get(loc)
        
        for i in range(0,max + 1):
            # print("i: ", str(i), " with val: ", str(p.val))
            if i == loc:
                Solution.cache[loc] = p.val
                return p.val
            p = p.next
    
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        Solution.cache = {}
        p1 = head
        tail = 0
        
        # Find the end.
        while p1 != None:
            p1 = p1.next
            tail = tail + 1

        if tail == 1 or tail == 0:
            return True


        # print("Items: ", tail)

        # find center and reset p2 pointer.
        midpoint = int(math.floor(tail/2))
        mv = 0  
        if tail%2 == 0:
            mv = 1
        p1 = head

        for i in range(0, midpoint):
            # print("i: ", str(i), " vs ", (tail-1) -i)
            # print("p1: ", p1.val, " vs ", self.getVal(head, (tail -1) - i, tail))

            if p1.val != self.getVal(head, (tail -1) - i, tail):
                # print("*** NO MATCH ***")
                return False
            
            p1 = p1.next

        '''
        for j in range(tail-1, midpoint - mv, -1):
            if(self.dynamicGetVal(head, (tail -1) - j,tail) != self.dynamicGetVal(head,j,tail)):
                return False
        '''

        return True
                
                

solution = Solution()

test1 = ListNode(1)
test1.next = ListNode(2)
test1.next.next = ListNode(3)
test1.next.next.next = ListNode(4)
test1.next.next.next.next = ListNode(5)
print(solution.isPalindrome(test1))

print("*********** SPLIT *************")

test2 = ListNode(1)
test2.next = ListNode(2)
test2.next.next = ListNode(2)
test2.next.next.next = ListNode(1)
print(solution.isPalindrome(test2))

print("*********** SPLIT *************")
test3 = ListNode(0)
test3.next = ListNode(0)
print(solution.isPalindrome(test3))