from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        return self.listToListNode(sorted(self.listNodeToList(l1) + self.listNodeToList(l2)))

    # Totally insane way to do this... Convert to a List
    def listNodeToList(self, head: ListNode) -> List[int]:
        p = head 
        oList = []

        while p != None:
            oList.append(p.val)
            p = p.next
            
        return oList

    # Convert the list back into a ListNode.
    def listToListNode(self, l: ListNode) -> ListNode:
        listNode = ListNode(l[0]) 
        p = listNode
        for i in range(1, len(l)):
            p.next = ListNode(l[i])   
            p = p.next

        return listNode

s = Solution()
l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)

l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

nachos = s.mergeTwoLists(l1, l2)
print(nachos)