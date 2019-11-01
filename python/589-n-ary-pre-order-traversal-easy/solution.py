from typing import List

# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Solution:
    def __init__(self):
        self.values = []

    def preorder(self, root: 'Node') -> List[int]:
        self.preorderHelper(root)
        return self.values

    def preorderHelper(self, root: 'Node') -> List[int]:
        if root is None:
            return None
        else:
            self.values.append(root.val)
            for c in root.children:
                self.preorder(c)

t1 = {"$id":"1","children":[{"$id":"2","children":[{"$id":"5","children":[],"val":5},{"$id":"6","children":[],"val":6}],"val":3},{"$id":"3","children":[],"val":2},{"$id":"4","children":[],"val":4}],"val":1}
t2 = Node(1, [Node(3, [None])])
s = Solution()
print(s.preorder(t2))