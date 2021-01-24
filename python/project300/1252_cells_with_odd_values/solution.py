from typing import List

class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        t = [[0 for i in range(m)] for j in range(n)]  
        total = 0

        # Apply our math to t.
        for i in indices:
            rowi = i[0]
            coli = i[1]
            # Only when we are on a target row or col.
            for row in range(n):
                for col in range(m):
                    if rowi == row: 
                        t[row][col] += 1

                    if coli == col:
                        t[row][col] += 1

        # Find odd values.
        for row in range(n):
            for col in range(m):
                if t[row][col] % 2 != 0:
                    total += 1

        return total
s = Solution()
print(s.oddCells(2,3,[[0,1],[1,1]]))