# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        v = []
        self.inOrder(root, v)
        return v

    def inOrder(self, root: TreeNode, v: List[int]):
        if root:
            self.inOrder(root.left, v)
            v.append(root.val)
            self.inOrder(root.right, v)
        