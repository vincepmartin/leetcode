from typing import List

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        properHeights = sorted(heights)
        differences = 0

        for i in range(len(heights)):
            if heights[i] != properHeights[i]:
                differences += 1

        return differences

s = Solution()
t1 = [1,1,4,2,1,3]
print(s.heightChecker(t1))