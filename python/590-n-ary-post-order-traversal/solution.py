# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return 

        results = []
        for c in root.children:
            results.append(c.val)
            self.postorder(c) 
        print(f'Root val {root.val}') 
        results.append(root.val)
        print(results)
        return results