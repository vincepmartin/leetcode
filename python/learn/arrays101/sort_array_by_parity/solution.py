from typing import List

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        lastOdd = 0
        i = 0

        # Split into two sections. [Even, Odd]
        for i in range(0, len(A)):
            if A[i] % 2 == 0: # we have an even.
                print("Let's swap some stuff:") 
                A[i], A[lastOdd] = A[lastOdd], A[i]
                lastOdd += 1

s = Solution()
t1 = [3,1,2,4]
t1s = [2,4,3,1]  
print(s.sortArrayByParity(t1))