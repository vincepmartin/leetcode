# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.max = 0

    def depthHelper(self, node):
        self.max = 0
        self.preOrder(node)
        return self.max

    def preOrder(self, node):
        if node != None:
            left = self.preOrder(node.left)
            right = self.preOrder(node.right)
            self.max = max(self.max, left + right + 1)
            return max(left, right) + 1

        return 0 

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if root == None:
            return 0 

        return self.depthHelper(root) - 1

s = Solution()
t = TreeNode(1)
t.left = TreeNode(2)
t.left.left = TreeNode(4)
t.left.right = TreeNode(5)
t.right = TreeNode(3)
print(s.diameterOfBinaryTree(t))