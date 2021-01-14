from typing import List

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        total = 0
        mask = self.makeMask(len(mat))
        for i in range(len(mat)):
            for j in range(len(mat)):
                if mat[i][j] * mask[i][j] != 0:
                    total += mat[i][j]

        return total

    def makeMask(self, n: int) -> List[List[int]]:
        m = [[0] * n for i in range(n)]
        for r in range(len(m) // 2):
            # Top
            m[r][r] = 1
            m[r][n-r-1] = 1

            # Bottom
            m[n-r-1][r] = 1
            m[n-r-1][n-r-1] = 1

        # Given an odd n we have to set the middle row.
        if n % 2 != 0:
            m[len(m)//2][len(m)//2] = 1

        return m

s = Solution()
print(s.diagonalSum([[1,2,3],[4,5,6],[7,8,9]]))