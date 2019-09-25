# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.total = 0

    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        self.rangeSumBSTUtil(root, L, R)
        return self.total

    def rangeSumBSTUtil(self, root: TreeNode, L: int, R: int) -> int:
        # Base case
        if root:
            self.rangeSumBSTUtil(root.left, L, R)
            if L <= root.val <= R:
                print(root.val)
                self.total += root.val 
            self.rangeSumBSTUtil(root.right, L, R)

s = Solution()

t1 = TreeNode(10)
t1.left = TreeNode(5)
t1.left.left = TreeNode(3)
t1.left.right= TreeNode(7)
t1.right = TreeNode(15)
t1.right.right = TreeNode(18)

print(s.rangeSumBST(t1, 7, 15))

