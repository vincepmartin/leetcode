from typing import List

class Solution:
    def tribonacci(self, n: int) -> int:
        # Populate our memo.
        memo = {0: 0, 1:1, 2:1}
        return(self.getTib(n, memo))


    def getTib(self, n: int, memo: List[int]) -> int: 
        # Our base case.
        if n < 0:
            return 0

        # Check our cache.
        if n in memo:
            return memo[n]

        # Not in cache, let's put it there.
        memo[n] = self.getTib(n - 3, memo) + self.getTib(n - 2, memo) + self.getTib(n - 1, memo)
        return memo[n]

s = Solution()
print(s.tribonacci(25))