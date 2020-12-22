'''
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
'''
from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        consecutive = 0
        maxConsecutive = 0
        for i in nums:
            if i != 0:
                consecutive += 1
            else:
                consecutive = 0

            # Adjust for new max
            if consecutive > maxConsecutive:
                maxConsecutive = consecutive

        return maxConsecutive

''' 
Test
'''

s = Solution()
t = [0,0,0,1,1,1,0,0]
print(s.findMaxConsecutiveOnes(t))