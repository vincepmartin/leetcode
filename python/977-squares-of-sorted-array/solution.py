from typing import List

class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        return self.sortedSquaresMap(A)

    def sortedSquaresListComprehension(self, A: List[int]) -> List[int]:
        squared = [(x*x) for x in A]
        squared.sort()
        return squared


    def sortedSquaresMap(self, A: List[int]) -> List[int]:
        squared = list(map(lambda x: x*x, A))
        squared.sort()
        return squared


s = Solution()
print(s.sortedSquares([-4,-1,0,3,10]))