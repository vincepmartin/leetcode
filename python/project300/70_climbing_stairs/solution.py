from typing import List

class Solution:
    def climbStairs(self, n: int) -> int:
        # Store cache for calculations.
        memo = {}

        return(self.countAllStairs(0, n, memo))

    def countAllStairs(self, currentStair: int, destinationStair: int, memo: List[int]) -> int:
        if currentStair > destinationStair:
            return 0

        if currentStair == destinationStair:
            return 1

        if currentStair in memo:
            return memo[currentStair]

        memo[currentStair] = self.countAllStairs(currentStair + 1, destinationStair, memo) + self.countAllStairs(currentStair + 2, destinationStair, memo)
        return memo[currentStair]
        
s = Solution()
print(s.climbStairs(2))
print(s.climbStairs(5))