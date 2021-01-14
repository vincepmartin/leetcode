from typing import List

class Solution:
    def myAtoi(self, s: str) -> int:
        if len(s) == 0:
            return 0

        ans = int(self.grabSignsAndNumbers(s))
        lower = pow(-2, 31)
        upper = pow(2, 31) - 1

        if ans < lower:
            return lower
        elif ans > upper:
            return upper

        return ans

    def grabSignsAndNumbers(self, s: str) -> str:
        lookupNumbers = {
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

        lookupSigns = {'+': None, '-': None}

        signsFound = 0
        good = []

        for i in s:
            # We have a good value.  Append to our list.
            if i in lookupNumbers:
                good.append(i)

            # We have a sign, append it if we have only one so far.  
            elif i in lookupSigns:
                signsFound += 1
                if signsFound >= 2:
                    return 0 
                good.append(i)

            
            # A non good character means terminate.
            elif i not in lookupNumbers and i != ' ':
                break

        # Sometimes we are empty.  Put a 0.
        if not good:
            good.append('0')

        return ''.join(good)

s = Solution()
'''
print(s.myAtoi("4193 with words"))
print(s.myAtoi('3.14159'))
print(s.myAtoi('-+12'))
print(s.myAtoi("+1"))
'''
print(s.myAtoi("   -42"))
