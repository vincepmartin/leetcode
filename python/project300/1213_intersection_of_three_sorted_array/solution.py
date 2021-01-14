from typing import List
class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        vals = {}

        def countVals(arr: List[int]):
            for i in arr:
                if i in vals:
                    vals[i] += 1
                else:
                    vals[i] = 1
        countVals(arr1)
        countVals(arr2)
        countVals(arr3)

        answer = []
        for i in vals.keys():
            if vals[i] == 3:
                answer.append(i)

        answer.sort()
        return answer

s = Solution()
print(s.arraysIntersection([1,2,3,4,5], [1,2,5,7,9], [1,3,4,5,8]))