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
        if not root:
            return []
        
        result = []
        for c in root.children:
            result.extend(self.preorder(c))

        return result

t2 = Node(1, [Node(3, [None])])
s = Solution()
print(s.preorder(t2))