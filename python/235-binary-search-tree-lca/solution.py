# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p,q)

        elif root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p,q)

        elif root.val == p.val or root.val == q.val:
            return root.val

        else:
            return root

    def wtf(self, a, b, c):
        print(a.val, b.val, c.val)


# Create some test data.

a = TreeNode(6)
a.left = TreeNode(2)
a.left.left = TreeNode(0)
a.left.right = TreeNode(4)
a.left.right.left = TreeNode(3)
a.left.right.right = TreeNode(5)

a.right = TreeNode(8)
a.right.left = TreeNode(7)
a.right.right = TreeNode(9)

b = TreeNode(2)
c = TreeNode(8)

test = Solution()

print ("lets try to do somethings...")
print(test.lowestCommonAncestor(a, b,c).val)

