from typing import List, Tuple

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # Temp store of our coin counts.
        coinTotal = 0

        while nums:
            # One left.
            if len(nums) == 1:
                coinTotal += nums[0]
                nums.pop(0)

            # Two left.
            if len(nums) == 2:
                coinTotal += nums[0] * nums[1]

                if nums[0] <= nums[1]:
                    nums.pop(0)
                else:
                    nums.pop(1)

            # More left.
            if len(nums) > 2:
                minPos, coinCount = self.getMinCoinCount(nums) 
                coinTotal += coinCount
                nums.pop(minPos)

        return coinTotal
    
    # Look through the nums List to find which position gives you the maximum coin value.
    def getMinCoinCount(self, nums: List[int]) -> Tuple[int, int]:
        minValue = nums[0] * nums[1] * nums[2]
        minPos = 1

        # Sometimes we have a list with 1 item.
        if len(nums) == 1:
            return 0, nums[0]

        # Otherwise walk through the list.
        for i in range(1, len(nums)-1):
            # Otherwise we are in the middle of array and can use left and right.
            if nums[i-1] * nums[i] * nums[i+1] < minValue:
                minValue = nums[i-1] * nums[i] * nums[i+1]
                minPos = i

        return  minPos, minValue

    # Look through the nums List to find which position gives you the maximum coin value.
    def getMaxCoinCount(self, nums: List[int]) -> Tuple[int, int]:
        maxValue = 0
        maxPos = None

        # Sometimes we have a list with 1 item.
        if len(nums) == 1:
            return 0, nums[0]

        # Otherwise walk through the list.
        for i in range(len(nums)-1):
            # Handle the begining of the array.
            if i == 0 and nums[i] * nums[i+1] > maxValue:
                maxValue = nums[i] * nums[i+1]
                maxPos = i

            # Handle the end of the array.
            elif i == len(nums)-1 and nums[i] * nums[i-1]:
                maxValue = nums[i] * nums[i-1]
                maxPos = i

            # Otherwise we are in the middle of array and can use left and right.
            elif nums[i-1] * nums[i] * nums[i+1] > maxValue:
                maxValue = nums[i-1] * nums[i] * nums[i+1]
                maxPos = i

        return  maxPos, maxValue

s = Solution()
t1 = [3,1,5,8]
t2 = [9,76,64,21]
print(s.maxCoins(t2))
