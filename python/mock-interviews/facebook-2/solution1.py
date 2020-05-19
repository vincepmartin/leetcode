class Solution:
    def romanToInt(self, s: str) -> int:
        romans = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000,
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900
        }
        total = 0
        i = 0
        while i < len(s):
            if len(s) - i >= 2:
                if s[i] + s[i+1] in romans:
                    total += romans[s[i] + s[i+1]]
                    i += 2

                else:
                    total += romans[s[i]]
                    i += 1
            else:
                total += romans[s[i]]
                i += 1

        return total

s = Solution()
t1 = 'III'
t2 = 'IV'
print(s.romanToInt(t2))
        