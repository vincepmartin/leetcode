# Implementing memoization!
class Solution:
    fibCache = {} 
    
    def fib(self, N: int) -> int:
        if N == 1 or N == 0:
            return N
        else:
            # Update fibCache.
            if N not in self.fibCache:
                self.fibCache[N] = self.fib(N-1) + self.fib(N-2)
            return self.fibCache[N]


    # slightly faster version.
    # Why?
    def fib2(self, N: int) -> int:
        if N == 1 or N == 0:
            return N
        else:
            # Update fibCache.
            if N in self.fibCache:
                return self.fibCache[N]
            
            else:
                self.fibCache[N] = self.fib(N-1) + self.fib(N-2)
                return self.fibCache[N]

s = Solution()
print(s.fib(10))