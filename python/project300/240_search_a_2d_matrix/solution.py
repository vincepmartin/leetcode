from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        print(f'Is {target} between {matrix[0][0]} and {matrix[-1][-1]}...')
        if target < matrix[0][0] or target > matrix[-1][-1]:
            print('NO!')
            return False

        print('YES!')
        
        # We have a single row, lets search it.
        if len(matrix) == 1:
            print('We have a single line, let\'s do some searching.')
            for i in matrix[0]:
                if i == target:
                    return True

            return False

        # Split into two sets of rows. 
        else:
            midPoint = len(matrix) // 2
            return self.searchMatrix(matrix[0:midPoint], target) or self.searchMatrix(matrix[midPoint:],target)

s = Solution()
t1 = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]

print(s.searchMatrix(t1, 16))