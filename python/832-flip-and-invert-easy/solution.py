from typing import List

class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        out = []

        for row in A:
            out.append(self.invertList(self.flip(row)))
        return out

    def flip(self, A: List[int]) -> List[int]:
        return reversed(A)

    def invertList(self, A: List[int]) -> List[int]:
        return [self.invertVal(i) for i in A]

    def invertVal(self, v: int) -> int:
        if v == 0:
            return 1
        elif v == 1:
            return 0

s = Solution()
t1 = [[1,1,0],[1,0,1],[0,0,0]]
print(s.flipAndInvertImage(t1))