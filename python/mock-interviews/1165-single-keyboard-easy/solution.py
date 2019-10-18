class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        pos = 0  
        totalMoves = 0

        for c in word:
            totalMoves += abs(keyboard.index(c) - pos)
            pos += keyboard.index(c) - pos

        return totalMoves

    # Make faster but use more memory with a dict.
    def calculateTime2(self, keyboard: str, word: str) -> int:
        pos = 0  
        totalMoves = 0
        keyDict = {}
        # Put keyboard into a dict key -> pos
        for i in range(0, len(keyboard)):
            keyDict[keyboard[i]] = i

        for c in word:
            totalMoves += abs(keyDict[c] - pos)
            pos += keyDict[c] - pos

        return totalMoves        
s = Solution()
print(s.calculateTime2('abcdefghijklmnopqrstuvwxyz', 'cba'))
print(s.calculateTime2('pqrstuvwxyzabcdefghijklmno', 'leetcode'))
        