class Solution:
    def reverse(self, x: int) -> int:
        
        isNeg = 0
        digits = []
        ans = 0

        # Are we negative?
        if x < 0:
            isNeg = -1
            x *= -1

        elif x >= 0:
            isNeg = 1
        
        # Pop the digits off.  Populate digits. 
        while x != 0:
            digits.append(x % 10)
            x = int(x / 10)

        # Create our answer with values from digits.
        tens = 1
        while digits:
            ans = digits.pop() * tens + ans
            tens *= 10

        # Return out value with the negative sign added again if needed.
        ans = isNeg * ans 

        # Check we are in range.
        if ans >= -pow(2,31) and ans <= pow(2,31) - 1:
            return ans
        else:
            return 0
s = Solution()
print(s.reverse(301))