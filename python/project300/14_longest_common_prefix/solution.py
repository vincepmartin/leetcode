from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        match = [] # hold our common prefix counts.
        words = len(strs) # length of words in our list.
        ans = [] # Our eventual answer.

        # Sometimes we get an empty.
        if len(strs) == 0:
            return ''

        # Populate match with our first word.
        for c in strs[0]:
            match.append({c: 1})

        # Do the rest of the words.
        for w in strs[1::]:
            for c in range(len(w)): # We only have to check as many chars as in our first word.
                if c < len(match) and w[c] == list(match[c].keys())[0]:
                    match[c][w[c]] += 1
                else: # We don't match, break out early.
                    break

        # Calculate our final answer using match.
        for i in match:
            if i[list(i.keys())[0]] == words:
                ans.append(list(i.keys())[0])

        # Join then return our answer in string form.
        return ''.join(ans)

s = Solution()
t1 = ["flower","flow","flight"]
t2 = ["dog"]
print(s.longestCommonPrefix(t2))