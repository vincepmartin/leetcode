from typing import List

class Solution:
    def anagramMappings(self, A: List[int], B: List[int]) -> List[int]:
        # Create a dict of mappings. 
        aDict = {}
        for i in range(0, len(B)):
            if B[i] in aDict:
                aDict[B[i]].append(i)
            else:
                aDict[B[i]] = [i] 

        # Process our dict to create a list.
        aMap = []
        for i in A:
            aMap.append(aDict[i].pop())

        return aMap


s = Solution()
print(s.anagramMappings([12, 28, 46, 32, 50], [50, 12, 32, 46, 28]))