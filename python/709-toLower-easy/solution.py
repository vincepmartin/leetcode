class Solution:
    def toLowerCase(self, word: str) -> str:
        upper = []
        # Let's use list comprehension.
        for c in word:
            if self.isLower(c):
                upper.append(self.makeCharLower(c))
            else:
                upper.append(c)

        return ''.join(upper)

    def makeCharLower(self, c: str) -> str:
        return chr(ord(c) +32)

    def isLower(self, c: str) -> bool:
        if ord(c) >= 65 and ord(c) <= 90:
            return True

s = Solution()
print(s.toLower('Nachos'))
print(s.toLower('TACOS'))
print(s.toLower('burritos'))