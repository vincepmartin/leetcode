from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # i + b = target
        
        for i in range(0, len(nums)):
            b = target - nums[i]
            print('b = target - nums[i] -> ', b, '=', target,'-',nums[i])
            
            # if b is in the nums list then we are good to go!
            if b in nums[i+1:]:
                return [i, nums.index(b, i+1)]

# Let us test!
s = Solution()
print(s.twoSum([3,2,4], 6))