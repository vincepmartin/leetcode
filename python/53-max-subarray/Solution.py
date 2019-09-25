class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        maxSoFar = nums[0]
        maxEndingHere = nums[0]

        for i in range(1, len(nums)):
            maxEndingHere = max(maxEndingHere + nums[i], nums[i])
            maxSoFar = max(maxSoFar, maxEndingHere)
        
        return maxSoFar

    
s = Solution()
t1 = [-2,1,-3,4,-1,2,1,-5,4]

print(s.maxSubArray(t1))