# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root == None:
            return True

        return self.isMirror(root.left, root.right)

    def isMirror(self, n1: TreeNode, n2: TreeNode) -> bool:
        if n1 == None and n2 == None:
            return True

        elif n1 == None or n2 == None:
            return False

        return (n1.val == n2.val) and self.isMirror(n1.left, n2.right) and self.isMirror(n1.right, n2.left)

s = Solution()
t1 = TreeNode(1)
t1.left = TreeNode(2)
t1.left.left = TreeNode(3)
t1.left.right = TreeNode(4)

t1.right= TreeNode(2)
t1.right.left = TreeNode(4)
t1.right.right = TreeNode(3)

print(s.isSymmetric(t1))