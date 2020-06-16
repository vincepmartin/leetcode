from typing import List

class Solution: 

    def replaceElements(self, arr: List[int]) -> List[int]:
        # Sanity checks.
        if len(arr) <= 1:
            return arr

        for i in range(len(arr) - 1):
            maxRight = max(arr[i + 1::])
            arr[i] = maxRight

        arr[-1] = -1
        return arr

s = Solution()
t1 = [17,18,5,4,6,1]

print(f"t1: {t1} turns into {s.replaceElements(t1)}")