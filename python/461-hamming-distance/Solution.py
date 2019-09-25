class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """

        # Convert both x and y to a binary string.
        xBin = "{:032b}".format(x)
        yBin = "{:032b}".format(y)
        hammingDistance = 0

        for i in range(0, len(xBin)):
            if xBin[i] != yBin[i]:
                hammingDistance += 1

        return hammingDistance

s = Solution()
print(s.hammingDistance(1, 4))
        