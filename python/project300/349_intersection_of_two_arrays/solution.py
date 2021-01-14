from typing import List
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        firstVals = {}

        # Create a lookup table for the first list of Nums.
        for i in nums1:
            firstVals[i] = True
        
        # Check this table for values in the second table. 
        answer = []
        for x in nums2:
            if x in firstVals and firstVals[x] != False:
                firstVals[x] = False
                answer.append(x)
        
        return answer       

s = Solution()
nums1 = [1,2,2,1]
nums2 = [2,2]
print(s.intersection(nums1, nums2))