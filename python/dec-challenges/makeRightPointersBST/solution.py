# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    depthMap = {}
    def connect(self, root: 'Node') -> 'Node':
        self.walkTreeInOrder(root, 0)
        
        for d in self.depthMap.keys():
            print(f'Depth: {d}')
            for n in range(len(self.depthMap[d]) - 1):
                if n != len(self.depthMap[d]) - 1:
                    self.depthMap[d][n].next = self.depthMap[d][n+1]

        return root

    def walkTreeInOrder(self, root, depth):
        if root != None:
            self.walkTreeInOrder(root.left, depth + 1)
            if depth in self.depthMap: 
                self.depthMap[depth].append(root)
            else: 
                self.depthMap[depth]=[root]
            self.walkTreeInOrder(root.right, depth + 1)

s = Solution()
t1 = Node(1)
t1.left = Node(2)
t1.left.left = Node(4)
t1.left.right = Node(5)
t1.right = Node(3)
t1.right.right = Node(7)

print(s.connect(t1))
