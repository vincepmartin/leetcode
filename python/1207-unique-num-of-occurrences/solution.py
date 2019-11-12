from typing import List

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        oc = {}

        for i in arr:
            if i in oc:
                oc[i] += 1
            else:
                oc[i] = 1

        ocCount = set()

        for (key, value) in oc.items():
            print(f'{key} - > {value}')
            if value in ocCount:
                return False
            
            else:
                ocCount.add(value)

        return True

s = Solution()
print(s.uniqueOccurrences([1,2,2,1,1,3]))
print(s.uniqueOccurrences([1,2]))
