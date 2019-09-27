# https://leetcode.com/problems/product-of-array-except-self/
from typing import List

class Solution:
    def productExceptSelfSlow(self, nums: List[int]) -> List[int]:
        p = [None] * len(nums)

        # Dumb way... O(n^2) due to calling an O(n) function n times...
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

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Done via hints from the solution.
        # Define a L and R array w/ products that accumulate.
        L = nums.copy()
        L[0] = 1

        R = nums.copy()
        R.reverse() 
        R[0] = 1

        print("Orig:")
        print(nums)

        #O(N) Calculate the products to the left of n 
        for i in range(1, len(nums)):
            L[i] = nums[i-1] * L[i-1]

        #O(N) Calculate the products to the right of n with same alg as above
        #with a flipped nums and then reverse.
        nums.reverse() 
        for i in range(1, len(nums)):
            R[i] = nums[i-1] * R[i-1]
        R.reverse()

        #O(N) Calculate each item. 
        for i in range(0, len(nums)):
            nums[i] = L[i] * R[i]

        #Above is O(3N) simplifies to O(N)
        return nums

s = Solution()
t1 = [1, 2, 3, 4]

print(s.productExceptSelf(t1))