from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.counts = {}

    def findMode(self, root: TreeNode) -> List[int]:
        if root == None:
            return list()

        self.setCounts(root)
        return self.findMaxVal(self.counts)

    def setCounts(self, root: TreeNode) -> List[int]:
        if not root:
            return None

        if root.val not in self.counts:
            self.counts[root.val] = 1
        else:
            self.counts[root.val] += 1

        self.findMode(root.left)
        self.findMode(root.right)

    # Find max value...
    # This is so so dumb I'm sure.  But I will try to do again. 
    def findMaxVal(self, x):
        maxList = []
        maxVal = max(self.counts.values())
        for key,val in self.counts.items():
            if val == maxVal:
                maxList.append(key)

        return maxList

t2 = TreeNode(2)
t2.left = TreeNode(1)
t2.left.right = TreeNode(4)
t2.right = TreeNode(4)
t2.right.right = TreeNode(7)        

s = Solution()
print(s.findMode(t2))