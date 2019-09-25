from typing import List

class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        # Flipped and inverted.
        B = []
        count = 0

        for row in A:
            temp = []
            while row:
                temp.append(self.invert(row.pop()))
            B.append(temp)
            count += 1
        return B

    def invert(self, val):
        if val == 0:
            return 1
        else:
            return 0


s = Solution()
t1 = [[1,1,0],[1,0,1],[0,0,0]]

print(s.flipAndInvertImage(t1))