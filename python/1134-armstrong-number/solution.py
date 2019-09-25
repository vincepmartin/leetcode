class Solution:
    def isArmstrong(self, N: int) -> bool:
        # Find number of digits in number.
        if N == 0:
            return False
        
        digits = int(math.log10(N) + 1)

        temp = N
        total = 0

        # Iterate though.
        while temp != 0:
            total += pow(int(temp%10), digits)
            temp = int(temp/10) # Take off one of the last digits.

        if total == N:
            return True

        return False