from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.mergeSort(nums)

    # This is what will be used recursively to sort our array.
    def mergeSort(self, nums: List[int]) -> List[int]:
        # Our base case will be when we have a list with only one item.
        if len(nums) <= 1:
            return nums

        # Otherwise keep going.
        left = self.mergeSort(nums[0: len(nums)//2])
        right = self.mergeSort(nums[len(nums)//2::])

        return self.merge(left, right)

    # This is what will be used to merge our array back together.
    def merge(self, l, r):
        merged = []
        lp = 0 
        rp = 0

        while lp < len(l) or rp < len(r):
            # We have processed our left list.  Just append something from the right.
            if lp >= len(l):
                merged.append(r[rp])
                rp += 1

            # We have processed our right list.  Just append something from the left.
            elif rp >= len(r):
                merged.append(l[lp])
                lp += 1

            # We have something left in both of our lists.  Now compare which is a smaller value and append that one.
            # Take a value from the left. 
            elif l[lp] <= r[rp]:
                merged.append(l[lp])
                lp += 1
            # Take a value from the right. 
            else:
                merged.append(r[rp])
                rp += 1

        return merged


s = Solution()
# print(s.merge([1,4,7], [2,3,10]))
# print(s.sortArray([5,2,3,1]))
print(s.sortArray([1]))