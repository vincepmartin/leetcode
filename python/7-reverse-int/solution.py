class Solution:

    # This is a solution using strings... This feels like cheating...
    def reverseUsingStrings(self, x:int) -> int:
        coeff = -1 if x < 0 else 1
        solution = coeff * int(''.join(list(str(abs(x)))[::-1]))
        bounds = pow(2,31)

        if solution <= -1 * bounds or solution >= bounds:
            return 0
        else:
            return solution

    # Let's try an actual math solution.
    def reverse(self, x:int) -> int:
        # How to get each digit? A: x % 10 gets us the last digit.
        nums = []
        coeff = -1 if x < 0 else 1
        x = abs(x)
        ans = 0 

        # Get each digit except for the last.
        while x >= 10:
            nums.append(x % 10)
            x = int(x / 10) # Gets us a floor.
        nums.append(x)

        print('nums:', nums)
        # Go through each, do the proper math to get us the answer.
        m = 1
        while nums:
            ans += nums.pop() * m
            m *= 10

        print('ans:', ans)
        if ans >= pow(2,31):
            return 0
        else:
            return coeff * ans

# test.
s = Solution()
print(s.reverse(1534236469))