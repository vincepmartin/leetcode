from typing import List

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        count = 0
        sortedHeights = sorted(heights)

        for i in range(0, len(heights)):
            if heights[i] != sortedHeights[i]:
                count += 1

        return count 

s = Solution()
t1 = [1,1,4,2,1,3]
print(s.heightChecker(t1))
