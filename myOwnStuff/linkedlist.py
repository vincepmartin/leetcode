class LinkedList:
    class Node:
        def __init__(self, val):
            self.val = val
            self.next = None

    def __init__(self, val):
        self.head = self.Node(val)
        self.tail = self.head 
        self.next = None 

    def add(self, val):
        self.tail.next = self.Node(val) 
        self.tail = self.tail.next

    def delete(self, val):
        pass

    def decapitate(self):
        val = self.head.val
        self.head = self.head.next
        return val

    def find(self, val):
        pass