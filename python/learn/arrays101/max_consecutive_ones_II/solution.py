from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        zeroLocs = []
        maxCount = 0

        # Find where zeroes are.
        for i in range(len(nums)):
            if nums[i] == 0:
                zeroLocs.append(i)

        # Sometimes we have no zero, lets just return the length then.
        if not zeroLocs:
            return len(nums)

        # Flip each one and then count consecutives ones.
        for z in zeroLocs:
            nums[z] = 1
            tempCount = 0
            tempMaxCount = 0

            for i in range(len(nums)):
                if nums[i] == 1:
                    tempCount += 1

                else:
                    if tempCount > tempMaxCount:
                        tempMaxCount = tempCount 
                    tempCount = 0

            if tempCount > tempMaxCount:
                tempMaxCount = tempCount 

            if tempMaxCount > maxCount:
                maxCount = tempMaxCount

            # Reset the zero
            nums[z] = 0

        return maxCount

s = Solution()
t1 = [1,0,1,1,0]
t2 = [1,1,0,1]
print(s.findMaxConsecutiveOnes(t2))