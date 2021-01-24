from typing import List

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        totalPairs = 0
        dominoPairs = {} 

        for d in dominoes:
            totalPairs += dominoPairs.get(str(sorted(d)), 0)

            # Cache our current results.
            dominoPairs[str(sorted(d))] = dominoPairs.get(str(sorted(d)), 0) + 1


        return totalPairs

s = Solution()
print(s.numEquivDominoPairs([[1,2],[1,2],[1,1],[1,2],[2,2]])) # 3
print(s.numEquivDominoPairs([[1,2],[2,1],[3,4],[5,6]])) # 1