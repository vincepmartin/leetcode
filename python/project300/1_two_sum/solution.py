from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            j = target - nums[i]
            
            try: # Get location of j if it exists.
                jLoc = nums.index(j)
                if jLoc != i:
                    return [i, jLoc]

            except:
                continue

s = Solution()
print(s.twoSum([3,3], 6))