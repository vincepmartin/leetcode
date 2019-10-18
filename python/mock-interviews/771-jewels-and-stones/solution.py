class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        count = 0
        jDict = {}

        for c in J:
            jDict[c] = None

        for c in S:
            if c in jDict:
                count += 1
        return count