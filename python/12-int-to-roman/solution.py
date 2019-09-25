class Solution(object):
    def intToRoman(self, num):
        """
        :type s: str
        :rtype: int
        """
        roman = ""

        while num > 0:
            if num in range(1,4):
                roman += "I"
                num -= 1
            elif num == 4:
                roman += "IV"
                num -= 4
            elif num == 5:
                roman += "V"
                num -= 5
            elif num in range(6,9):
                roman += "V"
                num -= 5
            elif num == 9:
                roman += "IX"
                num -= 9
            elif num == 10:
                roman += "X"
                num -= 10
            elif num in range (10, 40):
                roman += "X"
                num -= 10
            elif num == 40:
                roman += "XL"
                num -= 40
            elif num in range(41,50):
                roman += "XL"
                num -= 40
            elif num == 50:
                roman += "L"
                num -= 50
            elif num in range (51,90):
                roman += "L"
                num -= 50
            elif num == 90:
                roman += "XC"
                num -= 90
            elif num in range(91, 100):
                roman += "XC"
                num -= 90
            elif num == 100:
                roman += "C"
                num -= 100
            elif num in range(101, 400):
                roman += "C"
                num -= 100
            elif num == 400:
                roman += "CD"
                num -= 400
            elif num in range(401, 500):
                roman += "CD"
                num -= 400
            elif num == 500:
                roman += "D"
                num -= 500
            elif num in range(501, 900):
                roman += "D"
                num -= 500
            elif num == 900:
                roman += "CM"
                num -= 900
            elif num in range(901,1000):
                roman += "CM"
                num -= 900
            elif num == 1000:
                roman += "M"
                num -= 1000
            elif num > 1000:
                roman += "M"
                num -= 1000
        return roman

s = Solution()
tests = [39]

for t in tests:
    print("Testing: ", t, " -> ", s.intToRoman(t))
