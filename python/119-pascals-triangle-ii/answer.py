import math

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        returnList = list()
        for col in range(0, rowIndex + 1):
            returnList.append(self.getValue(rowIndex, col))

        return returnList

    def getValue(self, row, col):
        return(
            math.factorial(row) /(math.factorial(col) * math.factorial(row - col))
        )

solution = Solution()
print(solution.getRow(4))
