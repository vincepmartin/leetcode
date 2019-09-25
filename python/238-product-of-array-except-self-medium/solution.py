from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = [None] * len(nums)

        # Dumb way... O(n^2)
        for i in range(0, len(nums)):
            p[i] = self.productExceptN(nums,i)
        return p

    # This alone is O(N)
    def productExceptN(self, nums, n): 
        r = 1
        for i in range(0, len(nums)):
            if i != n:
                r *= nums[i]
        return r

s = Solution()
t1 = [1, 2, 3, 4]

print(s.productExceptSelf(t1))