class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        reverse = 0
        MIN = -2147483648
        MAX = 2147483647 
        coef = 1
        if x < 0:
            coef = -1

        # No checks for bounds are performed here.  I have to implement this.
        while x != 0:
            # Pop off a number from the end.
            pop = x % (coef * 10)
            print('Pop: ', pop)
            x = int(x / 10)
            print('New value for x: ', x)

            # Push that number onto reverse.
            temp = reverse * 10 + pop
            reverse = temp

        if reverse < MIN or reverse > MAX:
            return 0

        return reverse

test = Solution()


print(test.reverse(123))
print(test.reverse(-123))
