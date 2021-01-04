from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return self.prependZeroes(len(digits), self.getList(self.getInt(digits) + 1))

    def getInt(self, digits: List[int]) -> int:
        t = []
        for d in digits:
            t.append(str(d))

        return int(''.join(t))

    def getList(self, digits: int) -> List[str]:
        return list(str(digits))

    def prependZeroes(self, desired, digits) -> List[str]:
        t = []

        for i in range(desired - len(digits)):
            t.append('0')
        
        return t + digits


s = Solution()
print(s.plusOne([0,1]))
print(s.plusOne([1,2,3]))