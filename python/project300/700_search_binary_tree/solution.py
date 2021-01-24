# Definition for a binary tree node.
# class TreeNode:
def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root: 
            # Base case is we actually found what we are looking for.
            if root.val == val:
                return root
            
            if val < root.val:
                root = self.searchBST(root.left, val)
            
            elif val > root.val:
                root = self.searchBST(root.right, val)