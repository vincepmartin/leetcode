class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = 0
        flips = 0

        for c in s:
            if c == 'R':
                count += 1
            elif c == 'L':
                count -= 1

            # Check for difference in sign.
            if count == 0:
                flips += 1

        return flips

s = Solution()
t1 = 'RLRRLLRLRL'
t2 = 'RRLRLLR'
t3 = 'RLLLLRRRLR'       

print(t1, ':', s.balancedStringSplit(t1))
print(t2, ':', s.balancedStringSplit(t2))
print(t3, ':', s.balancedStringSplit(t3))