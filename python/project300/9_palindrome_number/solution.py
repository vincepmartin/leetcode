class Solution:
    def isPalindrome(self, x: int) -> bool:
        # A negative number is never a palindrome.
        if x < 0:
            return False

        if x == 0:
            return True

        digits = [] # Store our reverse x.

        while x != 0:
            digits.append(x%10)
            x = int(x / 10)
        
        digitsReverse = digits.copy()
        digitsReverse.reverse()

        for i in range(len(digits)):
            if digits[i] != digitsReverse[i]:
                return False
        
        return True

s = Solution()
t1 = 121
t2 = -121
t3 = 10
print(s.isPalindrome(t3))
        