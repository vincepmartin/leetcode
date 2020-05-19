from typing import List

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        total = 0

        for n in nums:
            if len(str(n)) % 2 == 0:
                total += 1

        return total

s = Solution()
print(s.findNumbers([12,345,2,6,7896]))
