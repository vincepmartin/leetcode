class Solution:
    def findDisappearedNumbers(self, nums):
        out = []
        if not nums:
            return out

        # Check all values in nums.
        # Example: [4,3,2,7,8,2,3,1] -> [5,6]
        for i in range(1, len(nums) + 1):
            tmp = nums[i-1]
            # Make the value negative.
            nums[abs(tmp) - 1] = abs(nums[abs(tmp) -1]) * -1

        # Anything that is positive means we do not have those values.
        for i in range(1, len(nums) + 1):
            if nums[i-1] > 0:
                out.append(i)
        return out
# Test
s = Solution()
print(s.findDisappearedNumbers([4,3,2,7,8,2,3,1]))
print(s.findDisappearedNumbers([2,2]))