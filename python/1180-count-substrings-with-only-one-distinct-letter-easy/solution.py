import math
class Solution:
    def countLetters(self, S: str) -> int:
        if S == '':
            return 0

        total = 0
        tempCount = 1
        lc = None

        for i in range (len(S)):
            if lc is None:
                lc = S[i] 
            
            # Last char does not match current.
            elif lc != S[i]:
                # Calculate total combinations. Reset tempCount. Set LC.
                total += self.nthTriangleNumber(tempCount)
                tempCount = 1
                lc = S[i]
            
            # Last char does match current.
            else:
                tempCount += 1
                lc = S[i]

        # Calculate remaining tempCount.
        total += self.nthTriangleNumber(tempCount)

        return math.floor(total)

    # An nth triangle is kind of like a factorial, but with addition instead.
    def nthTriangleNumber(self, n: int) -> int:
        return n*(n+1)/2

s = Solution()
print(s.countLetters('aaaba'))
# print(s.countLetters('yyyyyyyyyyyyyyyyyyyyyyyyyyykkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkhhhhhhhhhhhhhhhhhhmmkbbb'))