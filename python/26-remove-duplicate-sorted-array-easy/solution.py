from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int: 
        if len(nums) == 0 or nums is None:
            return 0

        if len(nums) == 1:
            return len(nums)

        p1 = 0
        p2 = 1
        count = 0

        while p2 != len(nums) - count - 1 and p1 != len(nums) - count - 2:
            if nums[p1] == nums[p2]:
                print('Moving', nums[p2])
                self.moveToEnd(p2, nums)
                count += 1
            else:
                p1 += 1
                p2 = p1 + 1

        print("I'm done doing stuff...")
        print(nums)
        return len(nums) - count

    # Move val at index p to end of list.
    def moveToEnd(self, p, nums):
        for i in range(p, len(nums) - 1):
            nums[i], nums[i+1] = nums[i+1], nums[i]

s = Solution()
print(s.removeDuplicates([1,1]))
print(s.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))