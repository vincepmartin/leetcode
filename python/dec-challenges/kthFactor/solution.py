class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factors = []
        for i in range(n, 0, -1):
            if n % i == 0:
                factors.append(int(n/i))
        if len(factors) < k:
            return -1
        else:
            return factors[k-1]

s = Solution()
print(s.kthFactor(7, 2))
