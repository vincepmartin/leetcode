from typing import List

class Solution:
    # O(N*N)  This is pretty bad, however, I can't imagine we'd have a ton of values.
    def calculateShortestDistance(self, a: List[int], b: List[int]) -> int:
        minDistance = None 
        
        for i in a:
            for j in b:
                d = abs(i - j)
                if minDistance == None or d < minDistance:
                    minDistance = d

        return minDistance
  
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        aIndexes = []
        bIndexes = []

        # O(N)
        for i in range(len(words)):
            if word1 == words[i]:
                aIndexes.append(i)
            elif word2 == words[i]:
                bIndexes.append(i)

        return self.calculateShortestDistance(aIndexes, bIndexes)

    

s = Solution()

t1 = ["practice", "makes", "perfect", "coding", "makes"]
print(s.shortestDistance(t1, "coding", "practice"))