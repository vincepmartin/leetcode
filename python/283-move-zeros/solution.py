class Solution(object):
    def swapValues(self, nums, j, k):
        nums[j], nums[k] = nums[k], nums[j]

    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        lz = 0
        for i in range(0, len(nums)):
            if nums[i] != 0:
                self.swapValues(nums, i, lz)
                lz += 1
s = Solution()

t1 = [0,1,0,3,12]
t2 = [0,1]
t3 = [0,1,0,3,12]
t4 = [0,0,0]

s.moveZeroes(t1)
print(t1)