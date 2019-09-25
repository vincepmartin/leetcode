# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.total = 0

    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.sumRights(root)
        return root

    # Do a RIGHT, THIS, LEFT traversal reverse-in-order and sum.
    def sumRights(self, root):
        if root is not None:
            # go right
            self.sumRights(root.right)        

            # go this
            self.total += root.val
            root.val = self.total 

            # go left
            self.sumRights(root.left) 

        return root

s = Solution()
t1 = TreeNode(5)
t1.left = TreeNode(2)
t1.right = TreeNode(13)
s.convertBST(t1)

