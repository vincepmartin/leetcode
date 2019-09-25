# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """

        # Let's traverse both trees and convert them to a list.
        sBucket = []
        self.lnr(s, sBucket, "r")

        tBucket = []
        self.lnr(t, tBucket, "r")

        if ''.join(tBucket) in ''.join(sBucket):
            return True

        else:
            return False

    # In order traversal.
    def lnr(self, node, bucket, ntype):
        if node != None:
            self.lnr(node.left, bucket, "l")
            bucket.append(str(node.val))
            self.lnr(node.right, bucket, "r")
        
        else:
            bucket.append(ntype + "N")
          

sol = Solution()

s = TreeNode(3)
s.left = TreeNode(4)
s.right = TreeNode(5)
s.left.left = TreeNode(1)
s.left.right = TreeNode(2)

t = TreeNode(4)
t.left = TreeNode(1)
t.right = TreeNode(2)
sol.isSubtree(s,t)