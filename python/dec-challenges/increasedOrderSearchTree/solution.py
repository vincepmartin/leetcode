# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    newTree = None
    maxNode = None

    def increasingBST(self, root: TreeNode) -> TreeNode:
        self.walkTreeInOrder(root) 
        return self.newTree

    #O(N)
    def walkTreeInOrder(self, root):
        if root != None:
            self.walkTreeInOrder(root.left)
            print(root.val)
            self.addToNewTree(root.val)
            self.walkTreeInOrder(root.right)
    # O(1)
    def addToNewTree(self, newVal):
        if self.newTree == None:
            self.newTree = TreeNode(newVal)
            self.maxNode = self.newTree

        else:
            self.maxNode.right = TreeNode(newVal)
            self.maxNode = self.maxNode.right


s = Solution()
t1 = TreeNode(5)
t1.left = TreeNode(3)
t1.left.left = TreeNode(2)
t1.left.right = TreeNode(4)
t1.left.left.left = TreeNode(1)
t1.right = TreeNode(6)
t1.right.right = TreeNode(8)
t1.right.right.left = TreeNode(7)
t1.right.right.right= TreeNode(9)

s.increasingBST(t1)