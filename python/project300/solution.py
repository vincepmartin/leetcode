from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [None] * len(nums)

        if len(nums) == 0:
            return 0

        if len(nums) == 1:
            return nums[0]

        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        # Calculate a List to store all of our possibilities up to i.
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])

        return dp[-1]

s = Solution()
print(s.rob([6,3,10,8,2,10,3,5,10,5,3]))