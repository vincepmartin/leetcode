from typing import List

class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        solutions = 0
        m = {}

        for a in A:
            for b in B:
                if a+b not in m:
                    m[a+b] = 1
                else:
                    m[a+b] += 1
        
        for c in C:
            for d in D:
                if -1 * (c + d) in m:
                    solutions += m[-1 * (c+d)]
        
        return solutions

s = Solution()
A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]
print(s.fourSumCount(A,B,C,D))
# print(s.fourSumCount([],[],[],[]))
