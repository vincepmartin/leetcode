from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''

        output = []
        matches = {}

        for i in range(0, len(min(strs, key = len))):
            matches.clear()

            for word in strs:
                if word[i] in matches:
                    matches[word[i]] += 1
                else:
                    matches[word[i]] = 1

            if len(matches) == 1:
                output.append(list(matches.keys())[0])
            
            else:
                return ''.join(output)

        return ''.join(output)

s = Solution()
print(s.longestCommonPrefix(['flower', 'flow', 'flight']))
print(s.longestCommonPrefix(['aca', 'cba']))