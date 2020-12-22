from typing import List
import math

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        total = 0
        maxA = 0

        # O(N)
        for n in nums:
            total += n

        # O(N)
        for n in nums:
            temp = math.floor(total / n)
            print(f'{temp} = {total} / {n}')

            if temp > maxA and temp <= threshold:
                print('new max')
                maxA = temp

        return maxA


s = Solution()
print(s.smallestDivisor([2,3,5,7,11], 11))