# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        x = self.llToString(l1)[::-1]
        y = self.llToString(l2)[::-1]
        
        return self.stringToLL(str(int(x)+int(y))[::-1]) 

    def llToString(self, node):
        if node == None:
            return ''
        if node != None:
            return str(node.val) + str(self.llToString(node.next))

    def stringToLL(self, s):
        node = ListNode(int(s[0]))
        p = node
        for i in range(1, len(s)):
            print(f'processing s[{i}]: {i}')
            p.next = ListNode(int(s[i]))
            p = p.next

        return node

s = Solution()
t1 = ListNode(2)
t1.next = ListNode(4)
t1.next.next = ListNode(3)

t2 = ListNode(5)
t2.next = ListNode(6)
t2.next.next = ListNode(4)
temp = s.addTwoNumbers(t1, t2)
print(temp)