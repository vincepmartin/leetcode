from typing import List

class Solution:
    def sumOfDigits(self, A: List[int]) -> int:
        # Find the smallest number.
        total = 0
        for c in str(sorted(A)[0]):
            print(c)
            total += int(c)


        if total % 2 == 0:
            return 1

        return 0