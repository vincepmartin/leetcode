# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.container = []
        self.current = 0
        self.root = root
        self.makeArray(root)

    def next(self) -> int:
        val = self.container[self.current]
        self.current += 1
        return(val)

    def hasNext(self) -> bool:
        if self.current < len(self.container):
            return True
        else:
            return False

    def makeArray(self, root):
        if root:
            self.makeArray(root.left)
            self.container.append(root.val)
            self.makeArray(root.right)

        


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