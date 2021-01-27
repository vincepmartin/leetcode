from typing import List

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = {} # A count of each number.
        totalPairs = 0
        for n in nums:
            count[n] = count.get(n, 0) + 1


        ''' 
        for c in count.keys():
            totalPairs += self.pairs(count[c])
        '''
        for c in count.values():
            totalPairs += c - 1

        return totalPairs

    def pairs(self, num:int) -> int: 
        total = 0
        for i in range(1, num):
            total += (1 * num - i)

        return total

s = Solution()
t1 = [1,2,3,1,1,3]
t2 = [1,1,1,1]
t3 = [1,2,3]
print(s.numIdenticalPairs(t1))
print(s.numIdenticalPairs(t2))
print(s.numIdenticalPairs(t3))