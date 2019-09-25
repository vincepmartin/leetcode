# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.max = 0

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0

        self.preOrder(root, 0)
        return self.max

    def preOrder(self, node, count):
        if node != None:
            count = count + 1
            if count > self.max:
                self.max = count
            
            self.preOrder(node.left, count)
            self.preOrder(node.right, count)

s = Solution()
t1 = TreeNode(3)
t1.left = TreeNode(9)
t1.right = TreeNode(20)
t1.right.left = TreeNode(15)
t1.right.right = TreeNode(7)

print(s.maxDepth(t1))