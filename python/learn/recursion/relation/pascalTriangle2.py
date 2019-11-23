from typing import List
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        return self.generate(rowIndex+1)[-1]

    def generate(self, numRows: int) -> List[List[int]]:
        # Sometimes someone stupid asks for 0.
        if numRows == 0:
            return []

        # Base case.
        if numRows == 1:
            return [[1]] 

        elif numRows == 2:
            return [[1],[1,1]]

        else:
            tempList = [None] * numRows
            tempList[0] = 1
            tempList[-1] = 1

            # Old list?
            generatedList = self.generate(numRows -1)

            for i in range(1, numRows-1):
                tempList[i] = generatedList[-1][i -1] + generatedList[-1][i]
            
            generatedList.append(tempList)
            return generatedList

s = Solution()
print(s.getRow(3))
