from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 0:
            return 0

        i = 0
        j = 1 
        swaps = 0

        #for j in range(i + 1, len(nums)):
        while j < len(nums) - 1: 
            if nums[j] == val:
                j += 1
            
            if nums[i] == val and nums[j] != val:
                nums[i], nums[j] = nums[j], nums[i]
                swaps += 1
                i += 1

            else:
                i += 1
                j += 1
        return i - 1

s = Solution()
t1 = [3,2,2,3]
print(f't old: {t1}')
print(s.removeElement(t1, 3))
print(f't new: {t1}')

t2 = [0,1,2,2,3,0,4,2]
print(f't old: {t2}')
print(s.removeElement(t2, 2))
print(f't new: {t2}')