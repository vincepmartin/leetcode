from typing import List
class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        countMap = {}

        for i in sorted(A):
            if i in countMap:
                countMap[i] += 1
            else:
                countMap[i] = 1

            if countMap[i] == len(A)/2:
                return i
            