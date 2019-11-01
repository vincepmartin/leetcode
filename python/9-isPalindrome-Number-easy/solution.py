class Solution:
    def isPalindrome(self, x: int) -> bool:
        if list(str(x)) == list(str(x))[::-1]:
            return True
        else:
            return False

s = Solution()
print('121', s.isPalindrome(121))
print('123', s.isPalindrome(123))
print('-123', s.isPalindrome(-123))
