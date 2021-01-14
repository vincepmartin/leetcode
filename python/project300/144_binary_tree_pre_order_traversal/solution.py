# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        v = []
        self.pot(root, v)
        return v

    def pot(self, root: TreeNode, v: List[int]):
        if root:
            v.append(root.val)
            self.pot(root.left, v)
            self.pot(root.right, v)