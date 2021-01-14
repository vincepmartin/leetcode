# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        v = []
        self.help(root, v)
        return v

    def help(self, root: TreeNode, v: List[int]):
        if root:
            self.help(root.left, v)
            self.help(root.right, v)
            v.append(root.val)