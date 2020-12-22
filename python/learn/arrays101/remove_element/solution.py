from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        matchCount = 0
        i = 0
        items = len(nums)
        
        while i < items - matchCount:
            if nums[i] == val:
                # print(f'{nums[i]} matches {val} i: {i}')
                self.shiftArrayLeft(nums, items, i)
                matchCount += 1
            
            else:
                # print(f'{nums[i]} no match {val} i: {i}')
                i += 1

        return items - matchCount

    def shiftArrayLeft(self, arr: List[int], arrLen: int, v: int):
        for i in range(v, arrLen - 1):
            arr[i] = arr[i+1]
        
s = Solution()
t1 = [1,2,3,4,5]
print(f't1: {t1}')
print(s.removeElement(t1, 3))
# s.shiftArrayLeft(t1, 2)
print(f't1: {t1}')