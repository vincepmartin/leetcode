from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        # Actual recursive function.
        def pot(root: TreeNode, values):
            if root == None:
                return

            pot(root.left, values)
            pot(root.right, values)
            values.append(root.val)
            return values

        return pot(root, [])

s = Solution()
t1 = TreeNode(3, TreeNode(2), TreeNode(4))
print(s.postorderTraversal(t1))