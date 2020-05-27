from typing import List

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        if len(arr) <= 1:
            return False

        for m in range(len(arr)):
            for n in range(len(arr)):
                if n != m and arr[n] == 2 * arr[m]:
                    print(f'arr[n]: {arr[n]} and arr[m]: {arr[m]}')
                    return True

        return False

s = Solution()
t1 = [-2,0,10,-19,4,6,-8]
print(s.checkIfExist(t1))