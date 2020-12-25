from typing import List
class Solution:
    minDistance = None
    minLoc = None

    def searchInsert(self, nums: List[int], target: int) -> int:
        ans = self.bSearch(nums, 0, len(nums) - 1, target)
        self.minDistance = None
        self.minLoc = None
        return ans

    def bSearch(self, nums, left, right, target):

        # Our base case.
        if right >= left:
            mid = left + ((right - left) // 2)
            currentDistance = abs(nums[mid] - target)

            if self.minDistance == None or currentDistance < self.minDistance:
                self.minDistance = currentDistance
                self.minLoc = mid

            if nums[mid] == target:
                return mid

            # We have a target that is less than our mid value.  Go left. 
            elif target < nums[mid]:
                return self.bSearch(nums, left, mid - 1, target)

            # We have a target that is more than our mid value. Go right.
            else:
                return self.bSearch(nums, mid + 1, right, target)

        # Not found, instead return our min Distance.
        else:
            if target > nums[self.minLoc]:
                return(self.minLoc + 1)
            else:
                return (self.minLoc)
s = Solution()
print(s.searchInsert([1,3,5,6], 3))
print(s.searchInsert([1,3,5,6], 5))
print(s.searchInsert([1,3,5,6], 2))
print(s.searchInsert([1,3,5,6], 7))
print(s.searchInsert([1,3,5,6], 0))
print(s.searchInsert([1], 0))
