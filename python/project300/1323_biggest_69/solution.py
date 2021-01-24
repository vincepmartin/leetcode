class Solution:
    def maximum69Number (self, num: int) -> int:
        numString = str(num)
        mostSigSix = numString.find('6')
        return int(numString[0:mostSigSix] + '9' + numString[mostSigSix + 1:])

s = Solution()
print(s.maximum69Number('9699'))