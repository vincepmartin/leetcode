import math

# Definition for singly-linked list.
class ListNode(object):
   def __init__(self, x):
       self.val = x
       self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        p1 = head
        tail = 0
        
        # Find the end.
        while p1 != None:
            p1 = p1.next
            tail = tail + 1

        # Quick checks.
        if tail == 1 or tail == 0:
            return True

        # print("Items: ", tail)

        # find center and reset p2 pointer.
        midpoint = int(math.floor(tail/2))
        mv = 0  
        if tail%2 != 0:
            mv = 1
        p1 = head

        # move p1 to midpoint.
        for c in range(0, midpoint + mv):
            p1 = p1.next

        # I know this is punk ass... Let's put the second half of this thing into a string and flip it.
        punkAss = []
        for c in range(midpoint + mv, tail):
            punkAss.append(p1.val)
            p1 = p1.next
        print(punkAss)
        punkAss.reverse()
        p1 = head

        # Special case w/ 3...
        if tail == 3:
            if p1.val == punkAss[0]:
                return True
            else:
                return False

        # Compare everything.
        print("midpoint: ", midpoint, " mv: ", mv)
        for i in range(0, midpoint):
            print("compare: ", str(p1.val), " and ", str(punkAss[i]))
            if p1.val != punkAss[i]:
                return False
            p1 = p1.next
        return True

solution = Solution()

test1 = ListNode(1)
test1.next = ListNode(2)
test1.next.next = ListNode(3)
test1.next.next.next = ListNode(4)
test1.next.next.next.next = ListNode(5)
print(solution.isPalindrome(test1))


print("*********** SPLIT *************")

test1a = ListNode(1)
test1a.next = ListNode(1)
test1a.next.next = ListNode(0)
test1a.next.next.next = ListNode(0)
test1a.next.next.next.next = ListNode(1)
print(solution.isPalindrome(test1a))


print("*********** SPLIT *************")
test2 = ListNode(1)
test2.next = ListNode(2)
test2.next.next = ListNode(2)
test2.next.next.next = ListNode(1)
print(solution.isPalindrome(test2))

print("*********** SPLIT *************")
test3 = ListNode(-1)
test3.next = ListNode(-1)
print(solution.isPalindrome(test3))

print("*********** SPLIT *************")
test4 = ListNode(1)
test4.next = ListNode(2)
test4.next.next = ListNode(1)
print(solution.isPalindrome(test4))

