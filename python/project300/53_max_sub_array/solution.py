from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        return self.helper(nums, 0, len(nums) - 1)

    def helper(self, nums: List[int], left, right) -> int:
        # Our base case is when our left and right pointer collide.
        # That basically means we have one value...  So our max is whatever that value is.
        if left == right:
            return nums[left]

        # Otherwise, lets do this thing.
        # Let's figure out what is max, our left side, our middle max or our right side.

        # First we have to find our middle point.
        middle = (left + right) // 2 # This will always give us 1 more on the left side than the right side.

        # Recursive calls.
        lmax = self.helper(nums, left, middle) # Our left side. From 
        mmax = self.maxSubArrayFromMiddle(nums, left, right)
        rmax = self.helper(nums, middle + 1, right) # Our right side with our middle + 1 so we have no overlap.

        # Return what is max.
        return max(lmax, mmax, rmax)

    def maxSubArrayFromMiddle(self, nums: List[int], left, right) -> int:
        maxLeft = float('-inf')
        maxRight = float('-inf')
        middle = (left + right) // 2

        # Find the max left starting at the middle.
        current = 0
        for i in range(middle, left - 1, -1):
            current += nums[i]
            maxLeft = max(current, maxLeft) 


        # Find the max right starting at middle + 1.
        current = 0
        for i in range(middle + 1, right + 1):
            current += nums[i]
            maxRight = max(current, maxRight) 

        return maxLeft + maxRight

s = Solution()
t1 = [-2,1,-3,4,-1,2,1,-5,4]
print(s.maxSubArray(t1))
print(s.maxSubArray([1,2]))