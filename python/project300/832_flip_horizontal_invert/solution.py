from typing import List

class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        
        for row in range(len(A)):
            # Reverse.
            A[row] = list(reversed(A[row]))
            # Invert.
            for a in range(len(A[row])):
                A[row][a] = A[row][a] ^ 1

        return A

s = Solution()
print(s.flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]]))
       