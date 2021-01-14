from typing import List
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        totalEvens = 0

        for i in nums:
            if self.isEven(i): 
                totalEvens += 1
        
        return totalEvens

    def isEven(self, n: int) -> bool:
        count = 0

        while n != 0:
            n = n // 10
            count += 1

        return count % 2 == 0

s = Solution()
t1 = [1,22,333,4444,55555]
print(s.findNumbers(t1))