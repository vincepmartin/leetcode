class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    
    def toString(self):
        p = self
        sList = ''
        
        if p.val == None:
            return ''

        while p != None:
            sList += str(p.val) + ' -> '
            p = p.next

        return sList

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Error conditions.
        if l1 is None and l2 is not None:
            return l2

        elif l1 is not None and l2 is None:
            return l1

        elif l1 is None and l2 is None:
            return None
 
        l3 = ListNode(None)
        p3 = l3

        while(l1 != None and l2 != None):
            if l1.val <= l2.val:
                if p3.val == None:
                    p3.val = l1.val
                    l1 = l1.next
                else: 
                    p3.next = ListNode(l1.val)
                    p3 = p3.next
                    l1 = l1.next

            elif l2.val < l1.val:
                if p3.val == None:
                    p3.val = l2.val
                    l2 = l2.next
                else: 
                    p3.next = ListNode(l2.val)
                    p3 = p3.next
                    l2 = l2.next

        '''
        l1 or l2 are now None.
        Empty the non None list into l3 and return l3.
        '''
        if l1 is None:
            self.emptyListInto(l2, p3)
        else:
            self.emptyListInto(l1, p3)

        return l3
        
    def emptyListInto(self, l1, l2):
        p1 = l1
        p2 = l2 
        while p1 != None:
            p2.next = ListNode(p1.val)
            p1 = p1.next
            p2 = p2.next

s = Solution()

t1 = None
t2 = ListNode(0)

print(s.mergeTwoLists(t1,t2).toString())