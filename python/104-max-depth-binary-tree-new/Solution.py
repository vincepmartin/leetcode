# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.md(root)

    def md(self, node):
        left = right = 0
        if node != None:
            left += self.md(node.left)
            right += self.md(node.right)
            return max(left, right) + 1
        else:
            return 0


s = Solution()
t1 = TreeNode(3)
t1.left = TreeNode(9)
t1.right = TreeNode(20)
t1.right.left = TreeNode(15)
t1.right.right = TreeNode(7)
print(s.maxDepth(t1))


s.maxDepth(t1)
        