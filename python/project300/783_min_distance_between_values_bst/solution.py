from typing import List
import sys

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    def minDiffInBST(self, root: TreeNode) -> int:
        minDiff = sys.maxsize 
        values = []
        self.inOrder(root, values)

        # We have populated our list of values in order.
        # Now we can O(N) run through them and calculate our smallest difference.        
        for i in range(0, len(values) - 1):
            minDiff = min(abs(values[i] - values[i+1]), minDiff)

        return minDiff

    def inOrder(self, root: TreeNode, values: List[int]) -> int:
        if root:
            self.inOrder(root.left, values)
            values.append(root.val)
            self.inOrder(root.right, values)

    '''
    def walkTree(self, root: TreeNode) -> int:
        # A base case is when we have no node.  So lets just return our smallest possible int.
        if not root:
            return 

        # Get our node values.
        lValue = self.walkTree(root.left)
        rValue = self.walkTree(root.right)

        # If they are not null, put them into our values List to find the min diff.
        values = []
        if lValue:
            values.append(abs(lValue - root.val))
        
        if rValue:
            values.append(abs(rValue - root.val))

        values.append(self.minDiff)
        self.minDiff = min(values)
        
        return root.val
    '''

s = Solution()
t1 = TreeNode(4)
t1.left = TreeNode(2)
t1.right = TreeNode(6)
t1.left.left = TreeNode(1)
t1.left.right = TreeNode(3)

print(s.minDiffInBST(t1))