# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        answer = self.listToInt(l1) + self.listToInt(l2)
        return self.intToList(answer)

    def listToInt(self, root):
        num = 0
        i = 1

        while root:
            num += root.val * i
            i *= 10
            root = root.next 

        return num

    def intToList(self, num):
        newList = ListNode(None)
        p = newList

        while num > 0:
            lastdigit = num % 10
            num = num//10

            if p.val == None:
                p.val = lastdigit
            
            else:
                p.next = ListNode(lastdigit)
                p = p.next

        if newList.val == None:
            newList.val = 0
        return newList

s = Solution()
a = ListNode(2)
a.next = ListNode(4)
a.next.next = ListNode(3)

b = ListNode(5)
b.next = ListNode(6)
b.next.next = ListNode(4)


t1 = ListNode(1)
t2 = ListNode(1)

print(s.intToList(1001))
print(s.listToInt(s.intToList(1000000000000000000000000000001)))

#print(s.listToInt(s.addTwoNumbers(t1,t2)))
