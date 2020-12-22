from typing import List

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        # Hold max values: [largest, 2nd largest, 3rd largest].
        maximumValues = [None, None, None]
        
        for i in range(len(maximumValues)):
            # print(f'*** Running #{i}')
            maximumValues[i] = self.findMaxExcluding(nums, maximumValues)

        # Return the proper value.
        # print('Checking maximumValues:')
        # print(maximumValues)

        if maximumValues[2] != None:
            return maximumValues[2]
        else:
            return maximumValues[0]

    def findMaxExcluding(self, nums, excludes):
        currentMax = None

        # O(N)
        for i in nums:
            if currentMax == None and i not in excludes:
                currentMax = i

            elif currentMax != None and i > currentMax and i not in excludes:
                # print(f'i: {i} vs currentMax: {currentMax}')
                # print('excludes')
                # print(excludes)
                currentMax = i

        # print(f'Current max is: {currentMax}') 
        return currentMax

s = Solution()
t0 = [3,2,1]
t1 = [1,2]
t2 = [2,2,3,1]

print(s.thirdMax(t0))