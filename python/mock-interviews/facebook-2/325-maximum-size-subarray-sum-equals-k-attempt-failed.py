from typing import List

class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        i = 0
        j = 0
        
        if nums is None or len(nums) == 0:
            return 0

        if len(nums) == 1 and nums[0] == k:
            return 1
        
        possibleAnswers = 0
        tempSum = 0
        answerHit = False
        
        for i in range(0, len(nums)):
            tempSum = 0
            tempSum += nums[i]
            if tempSum == k:
                return 1

            for j in range(i+1, len(nums)):
                tempSum += nums[j]

                # We have a match, record it and then reset tempSum.
                if tempSum == k:
                    answerHit = True 
                    if j - i > possibleAnswers:
                        possibleAnswers = j + 1 - i 
                    tempSum = 0
       
        if answerHit == False:
            return 0
        
        return possibleAnswers
s = Solution()
print(s.maxSubArrayLen([-1,1],-1))