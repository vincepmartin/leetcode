class Solution:
    def __init__(self):
        self.cache = {}

    def climbStairs(self, n: int) -> int:
        if n == 2:
            return 2

        elif n == 1:
            return 1

        if n not in self.cache:
            self.cache[n] = self.climbStairs(n-2) + self.climbStairs(n-1)

        return self.cache[n]

s = Solution()
# Should be 21.
print(s.climbStairs(7))