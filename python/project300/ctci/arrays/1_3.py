from typing import List
class Solution:
    def shiftRight(self, s: List[str], l: int, n: int):
        for i in range(len(s) - 1, l+n, -1):
            s[i], s[i-n] = s[i-n], s[i]


s = Solution()
t = list('a bc  ')
s.shiftRight(t, 1, 2)
print(t)