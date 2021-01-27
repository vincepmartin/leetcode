class Solution:
    def toLowerCase(self, str: str) -> str:
        # Figure out how much we have to subtract to create a lower case char.
        # Kind of ghetto... I'm sure I could just make this a constant...
        n = ord('A') - ord('a')

        # Create an empty List to store our value.
        lower = []

        # Loop through str and figure out if we have to convert.
        for c in str:
            if ord(c) >= 65 and ord(c) <= 90:
                lower.append(chr(ord(c) - n))
            else:
                lower.append(c)

        return ''.join(lower)

s = Solution()
print(s.toLowerCase('##NAchOS'))