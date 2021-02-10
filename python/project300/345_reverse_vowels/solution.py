class Solution:
    def reverseVowels(self, s: str) -> str:
        v = {'a': True, 'e': True, 'i': True, 'o': True, 'u': True}
        iofV = [i for i in range(len(s)) if v.get(s[i].lower())]
        vinS = ([c for c in s if v.get(c.lower())])
        sL = list(s)

        for i in iofV:
            sL[i] = vinS.pop()

        return ''.join(sL)

s = Solution()
print(s.reverseVowels('hello'))
print(s.reverseVowels('aA'))





