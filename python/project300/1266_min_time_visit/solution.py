from math import pow, sqrt
from typing import List

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        total = 0

        for i in range(len(points) - 1):
            total += self.findTimeBetween(points[i], points[i+1])

        return total

    def findTimeBetween(self, a: List[int], b: List[int]) -> int:
        diffX = abs(a[0] - b[0])
        diffY = abs(a[1] - b[1])
        return min(diffX, diffY) + (max(diffX, diffY) - min(diffX, diffY))

s = Solution()
t1 = [[1,1],[3,4],[-1,0]]
print(s.minTimeToVisitAllPoints([[3,2],[-2,2]]))