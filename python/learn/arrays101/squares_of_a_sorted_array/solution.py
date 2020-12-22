from typing import List

class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        return sorted([x*x for x in A])


s = Solution()
t1 = [-4,-1,0,3,10]

print(s.sortedSquares(t1))