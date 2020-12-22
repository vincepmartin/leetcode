# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.root = root    
        self.count = -1
        self.current = 0
        self.currentVal = None 
        self.total = 0
        self.totalNodes(root)

    def next(self) -> int:
        self.count = -1
        self.updateCurrentValue(self.root)
        self.current += 1
        return self.currentVal

    def hasNext(self) -> bool:
        if self.current < self.total:
            return True
        else:
            return False

    def total(self) -> int:
        return self.total

    def totalNodes(self, root):
        if root:
            self.totalNodes(root.left)
            self.total += 1
            self.totalNodes(root.right)

    def updateCurrentValue(self, root):
        if root and self.count < self.current:
                self.updateCurrentValue(root.left)
                self.count += 1 
                if self.count == self.current:
                    self.currentVal = root.val
                self.updateCurrentValue(root.right)

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

t1 = TreeNode(50)
t1.left = TreeNode(30)
t1.left.left = TreeNode(20)
t1.left.left.left = TreeNode(10)
t1.right = TreeNode(70)
t1.right.right = TreeNode(80)
t1.right.right.right = TreeNode(100)

b = BSTIterator(t1)

while b.hasNext():
    print(b.next())