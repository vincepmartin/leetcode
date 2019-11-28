class Solution:
    def climbStairs(self, N: int) -> int:
        # A cache to store some of our already calculated fibs.
        cache = {}

        # Define our recursive fib function.
        def fibr(n: int) -> int:
            if n == 0 or n == 1:
                return n

            elif n in cache:
                return cache[n]

            cache[n] = fibr(n-2) + fibr(n-1)
            return cache[n]

        fibr(N)
        print(cache)

        total = 0
        for v in cache.values():
            total += v

        return total

s = Solution()
print(s.fib(3))