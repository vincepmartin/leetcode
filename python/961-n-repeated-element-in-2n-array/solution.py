from typing import List

class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        return self.repeatedNTimesNoMap(self, A)

    def repeatedNTimesMap(self, A: List[int]) -> int:
        countMap = {}
        trigger = len(A)/2

        for i in A:
            if i in countMap:
                countMap[i] += 1
                if countMap[i] == trigger:
                    return i 
            else:
                countMap[i] = 1

    '''
    The map method works.  But this one is way faster.
    We benefit from the fact that each item in our array is unique except for
    the items that are repeated. 

    This lets us use a much faster datastructure! 
    '''
    def repeatedNTimesNoMap(self, A: List[int]) -> int:
        L = []

        for i in A:
            if i in L:
                return i
            else:
                L.append(i)

s = Solution()
print(s.repeatedNTimes([1,2,3,3]))