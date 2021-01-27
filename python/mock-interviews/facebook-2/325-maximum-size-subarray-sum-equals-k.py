from typing import List

class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        # Generate our prefix sum array.
        pS = self.prefixSumArray(nums)

        # Special case with only one item.
        if len(nums) == 1:
            if nums[0] == k:
                return 1
            else:
                return 0

        maxRange = 0
        for i in range(len(pS)):
            if nums[i] - k in pS:
                if i - pS.index(nums[i] - k) >= maxRange:
                    maxRange = i - pS.index(nums[i] - k) + 1

        return maxRange


    def prefixSumArray(self, nums: List[int]) -> List[int]:
        pSum = 0
        pS = [None] * len(nums)

        for i in range(len(nums)):
            pSum += nums[i]
            pS[i] = pSum        

        return pS

s = Solution()
tests2 = {1: [-2, -1, 2, 1], 3: [1, -1, 5, -2]}

# nums, k, answer
tests = [
    [[1, -1, 5, -2, 3], 3, 4],
    [[-2, -1, 2, 1], 1, 2],
    [[1], 1, 1],
    [[0,0],0,2]
]

for test in tests:
    nums, k, answer = test
    testResult = s.maxSubArrayLen(nums,k)
    print(f'Testing {nums} with k: {k}')
    print(f'\ttestResult: {testResult} answer: {answer}') 
    if(testResult != answer):
        print('\tTEST FAILED!')
    else:
        print('\tSUCCESS!')