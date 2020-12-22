from typing import List

class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        missingPairs = []

        # Special case with no entries in List.
        if len(nums) == 0:
            temp = self.findMissing(lower - 1, upper + 1)
            if temp:
                missingPairs.append(temp)
                return missingPairs

        # Handle lower.
        temp = self.findMissing(lower - 1, nums[0])
        if temp:
            missingPairs.append(temp)

        # Handle in between.
        for i in range(1, len(nums)):
            temp = self.findMissing(nums[i-1], nums[i])
            if temp:
                missingPairs.append(temp)

        # Handle upper.
        temp = self.findMissing(nums[-1], upper + 1)
        if temp:
            missingPairs.append(temp)

        return missingPairs


    def findMissing(self, a:int, b:int) -> str:
        if b - a > 1:
            if b - 1 != a + 1:
                return(str(a+1) + '->' + str(b-1))
            else:
                return(str(a+1))
        else:
            return None

s = Solution()
nums = []
lower = 1
upper = 1
# print(s.findMissing(0,4))
print(s.findMissingRanges(nums, lower, upper))