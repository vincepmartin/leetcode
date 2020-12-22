from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        temp = [None] * len(nums)
        ans = []

        for i in nums:
            temp[i-1] = i

        for i in range(len(nums)):
            if temp[i] == None:
                ans.append(i+1)

        return ans

s = Solution()
t1 = [4,3,2,7,8,2,3,1]
print(s.findDisappearedNumbers(t1))