class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        splitString = s.split()

        if len(splitString) == 0:
            return 0
        else:
            return len(splitString[-1])


s = Solution()
print(s.lengthOfLastWord('hello world'))
print(s.lengthOfLastWord(' '))