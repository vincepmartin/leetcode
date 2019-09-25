from typing import List

class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        evens = []
        odds = []
        sList = [] 
        
        # Split the values into two different arrays.
        for i in A:
            if i % 2 == 0:
                evens.append(i)  
            else:
                odds.append(i)

        # Insert items into the new list.
        for i in range(0, len(A)):
            if i % 2 == 0:
                sList.append(evens.pop())
            else:
                sList.append(odds.pop())

        return sList
            
s = Solution()
t1 = [4,2,5,7]

print(s.sortArrayByParityII(t1))