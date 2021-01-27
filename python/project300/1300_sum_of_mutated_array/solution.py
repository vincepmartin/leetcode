from typing import List

class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        arr.sort()
        arrSums = list(arr)

        # Store our smallest difference and it's index in arr.
        sd = float('inf')
        sdIndex = 0

        for i in range(1, len(arr)):
            arrSums[i] = arrSums[i-1] + arrSums[i]

        print(arr)
        print(arrSums)

        for i in range(len(arr)):
            print(f'Testing: {arr[i]}')
            # Get the left side total.
            leftSideTotal = 0
            if i > 0:
                leftSideTotal = arrSums[i-1]

            # Get the right side total.
            rightSideTotal = 0
            if i < len(arr):
                rightSideTotal = arr[i] * (len(arr) - i)

            if abs((leftSideTotal + rightSideTotal) - target) < sd:
                sd = abs((leftSideTotal + rightSideTotal) - target)  
                sdIndex = i 
            elif abs((leftSideTotal + rightSideTotal) - target) >= sd :
                break

        return arr[sdIndex]

arr = [4,9,3]
target = 10

s = Solution()
# print(s.findBestValue([4,9,3], 10))
print(s.findBestValue([60864,25176,27249,21296,20204],56803))
