class Solution:
    def reverseWords(self, s: str) -> str:
        reversedSentence = ''

        for word in s.split(' '):
            reversedSentence += ''.join(list(word)[::-1]) + ' '

        # Knock the last space off.
        return reversedSentence.rstrip()

# Test.
s = Solution()
print(s.reverseWords("Let's take LeetCode contest"))
