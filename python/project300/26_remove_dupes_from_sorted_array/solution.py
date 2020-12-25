from typing import List 

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Bail early if we have a list with 0 values.
        if len(nums) == 0:
            return 0

        i = 0

        # Otherwise lets do this.
        for j in range(i + 1, len(nums)):
            if nums[i] != nums[j]:
                nums[i+1] = nums[j]
                i += 1

        return i + 1

        

s = Solution()
t1 = [1,1,2]
print(f't old: {t1}')
print(s.removeDuplicates(t1))
print(f't new: {t1}')

t2 = [0,0,1,1,1,2,2,3,3,4]
print(f't old: {t2}')
print(s.removeDuplicates(t2))
print(f't new: {t2}')