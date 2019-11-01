class Solution:
    def removeVowels(self, S: str) -> str:
        rString = ''

        for c in S:
            if c not in ['a', 'e', 'i', 'o', 'u']:
                rString += c

        return rString