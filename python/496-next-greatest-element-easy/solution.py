from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output = []

        for n in nums1:
            output.append(self.nextGreatestNum(n, nums2))

        return output

    def nextGreatestNum(self, num: int, nums: List[int]) -> int:
        for n in nums[nums.index(num):]:
            if n > num:
                return n 

        return -1

s = Solution()
t1a = [4,1,2]
t1b = [1,3,4,2]
print(s.nextGreaterElement(t1a, t1b))