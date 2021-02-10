class Solution:
    def removeVowels(self, s: str) -> str:
       v = {'a': True, 'e': True, 'i': True, 'o': True, 'u': True} 
       return ''.join([i for i in s if v.get(i) == None])

s = Solution()
print(s.removeVowels('leetcodeisacommunityforcoders'))
print(s.removeVowels('aeiou'))
