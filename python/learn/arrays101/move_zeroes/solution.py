from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        j = len(nums) - 1

        # Let us bail out if there is nothing to do.
        if j <= 0:
            return

        i = j - 1
        oldI = i

        while i >= 0:
            if nums[i] == 0:
                oldI = i
                for i in range(i, j):
                    nums[i],nums[i+1] = nums[i+1], nums[i]
                j -= 1
                i = oldI 

            i -= 1

    def moveZeroes2(self, nums:List[int]) -> None:
        lastNonZero = 0

        for i in range(0, len(nums)):
            if nums[i] != 0:
                nums[lastNonZero] = nums[i]
                lastNonZero += 1

        for i in range(lastNonZero, len(nums)):
            nums[i] = 0


s = Solution()
t1 = [0,1,0,3,12]  
t1s = [1,3,12,0,0]

print(f"t1 was: {t1}")
s.moveZeroes2(t1)
print(f"t1 now is: {t1}")
print(f"t1 should be: {t1s}")