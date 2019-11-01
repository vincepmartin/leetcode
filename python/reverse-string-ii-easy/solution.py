class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        outputString = ''

        # grab len(2k) chunks from from s.
        for i in range(0, len(s), 2*k):

            # Figure out the end of our temp string.
            endVal = (i + 2*k) if (i + 2*k < len(s)) else len(s)

            # Get string to eval.
            tString = s[i:endVal]
            ''' 
            Remember that list[::-1] returns a new list that is reversed!  
            unlike reverse which requires a new line and is in place.
            '''
            outputString += ''.join(list(tString)[:k][::-1]) + tString[k:endVal]

        return outputString

# test this thing.
s = Solution()
print(s.reverseStr('abcdefg', 2))
