"""
Do not return anything, modify arr in-place instead.
"""
from typing import List

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        i = 0
        while i < len(arr):
            if arr[i] == 0:
                self.shiftToRight(i, arr)
                i += 2
            else:
                i += 1

    def shiftToRight(self, i, arr):
        t = arr[i]
        for i in range(i, len(arr) - 1):
            arr[i+1], t = t, arr[i+1]


s = Solution()
t1 = [1,0,2,3,0,4,5,0]
t2 = [1,2,3]

print(t1)
print(t2)
s.duplicateZeros(t1)
s.duplicateZeros(t2)
print(t1)
print(t2)