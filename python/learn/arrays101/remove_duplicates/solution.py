from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int: 
        a = 0
        b = a + 1
        end = len(nums) - 1

        while b <= end:
            if nums[a] != nums[b]:
                nums[a+1] = nums[b]
                a += 1
            
            else :
                b += 1

        return a + 1

s = Solution()
t1 = [1,1,1]
t2 = [0,0,1,1,1,2,2,3,3,4]
print(f'Before: {t1}')
print(f'New length: ${s.removeDuplicates(t1)}')
print(f'After: {t1}')