from typing import List

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        odds = []
        evens = []

	#O(N)
        for i in A:
            if i%2 == 0:
                evens.append(i)
            else:
                odds.append(i)

        # Is this O(N) again?
        return evens + odds

s = Solution()
print(s.sortArrayByParity([3,1,2,4]))