class Solution:
    def isPalindrome(self, x: int) -> bool:
        if str(x) == str(x)[::-1]:
            return True
        else:
            return False

s = Solution()
print(s.isPalindrome(121))
print(s.isPalindrome(-121))