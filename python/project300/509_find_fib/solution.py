from typing import List

class Solution:
    def fib(self, n: int) -> int:
        memo = {0:0, 1:1}
        return self.findFib(n, memo)

    def findFib(self, n: int, memo: List[int]) -> int:
        # Base case of n<0
        if n < 0:
            return 0

        if n in memo:
            return memo[n]

        memo[n] = self.findFib(n - 1, memo) + self.findFib(n - 2, memo)
        return memo[n]

s = Solution()
for i in range(0, 5):
    print(f'{i} is fib {s.fib(i)}\n')