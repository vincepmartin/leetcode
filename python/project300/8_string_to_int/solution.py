from typing import List

class Solution:
    def myAtoi(self, s: str) -> int:
        ans = int(self.grabSignsAndNumbers(s))
        lower = pow(-2, 31)
        upper = pow(2, 31) - 1

        if ans < lower:
            return lower
        elif ans > upper:
            return upper

        return ans

    def grabSignsAndNumbers(self, s: str) -> str:
        lookup = {
            '-': None,
            '0': None,
            '1': None,
            '2': None,
            '3': None,
            '4': None,
            '5': None,
            '6': None,
            '7': None,
            '8': None,
            '9': None
        }

        signFound = False

        good = []

        for i in s:
            if i in lookup:
                signFound = True
                good.append(i)
            else:
                if signFound == False and i != ' ':
                    return '0'

        return ''.join(good)

s = Solution()

# print(s.myAtoi("4193 with words"))
print(s.myAtoi('-91283472332'))
