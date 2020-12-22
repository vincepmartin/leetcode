from typing import AnyStr


class Solution:
    def romanToInt(self, s: str) -> int:
        lookup = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900
        }
        ans = 0
        skip = False

        for i in range(len(s)):
            if skip:
                skip = False
                continue

            # we are not on the last item.
            if i != len(s) - 1:
                if s[i] + s[i+1] in lookup:
                    ans += lookup[s[i] + s[i+1]]
                    skip = True
                else:
                    ans += lookup[s[i]]
                    skip = False

            else:
                ans += lookup[s[i]] 
                skip = False

        return ans
s = Solution()
t1 = 'III'
t2 = 'IV'
t3 = 'CD'
t4 = 'IX'

print(s.romanToInt(t1))