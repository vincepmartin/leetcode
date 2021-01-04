from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(len(nums2)):
            m = self.insertIntoArray(nums1, nums2[i], m)

        print(nums1) 
    
    def insertIntoArray(self, nums: List[int], x: int, m: int) -> None:
        for i in range(len(nums)):
            if nums[i] > x or i >= m:
                nums[m] = nums[i]
                nums[i] = x
                break
        return m + 1

s = Solution()
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

s.merge(nums1, m, nums2, n)
#s.insertIntoArray([1,2,10,0,0,0], 7, 3)        