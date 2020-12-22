from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # Actual recursive function.
        def iot(root: TreeNode, values):
            if root == None:
                return

            iot(root.left, values)
            values.append(root.val)
            iot(root.right, values)
            return values

        return iot(root, [])

s = Solution()
t1 = TreeNode(3, TreeNode(2), TreeNode(4))
print(s.inorderTraversal(t1))