from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        newNums = []

        for i in nums:
            newNums.append(i*i)

        newNums.sort()
        return newNums

s = Solution()
t1 = [-4,-1,0,3,10]
print(s.sortedSquares(t1))