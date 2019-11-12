import math

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        rvals = []

        for i in range(left, right + 1):
            if self.isDivByAll(i):
                rvals.append(i)

        return rvals

    def isDivByAll(self, numval):
        div = False

        if '0' not in str(numval):
            for s in str(numval):
                if numval % int(s) == 0:
                    div = True
                else:
                    return False

        return div

s = Solution()
print(s.selfDividingNumbers(1, 22))
# print(s.isDivByAll(21))