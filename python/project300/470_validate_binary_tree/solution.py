# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    last = float('-inf')

    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True

        if not self.isValidBST(root.left):
            return False
        
        if not self.addAndCheck(root.val):
            return False
        
        return self.isValidBST(root.right)

                
    def addAndCheck(self, val: int) -> bool:
        print(f'Checking if {val} is greater than {self.last}')
        if val > self.last:
            self.last = val
            return True
        
        return False


s = Solution()
t1 = TreeNode(2)
t1.left = TreeNode(1)
t1.right = TreeNode(3)


t2 = TreeNode(5)
t2.left = TreeNode(1)
t2.right = TreeNode(4)
t2.right.left = TreeNode(3)
t2.right.right = TreeNode(6)

t3 = TreeNode(1)
t3.left = TreeNode(1)

t4 = TreeNode(5)
t4.left = TreeNode(4)
t4.right = TreeNode(6)
t4.right.left = TreeNode(3)
t4.right.right = TreeNode(7)

t5 = TreeNode(5)
t5.left = TreeNode(1)
t5.right = TreeNode(4)
t5.right.left = TreeNode(3)
t5.right.right = TreeNode(6)

print(s.isValidBST(t5))