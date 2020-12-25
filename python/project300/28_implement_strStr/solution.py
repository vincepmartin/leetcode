class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # What we are going to do is iterate through haystack. from 0 to len(haystack) - len(needle)    
        location = -1
        lh = len(haystack)
        ln = len(needle)

        if ln == 0:
            return 0

        if ln == 0 and lh == 0:
            return 0

        # Calculate range for our loop.
        loopRange = lh
        if ln > 1:
            if lh - ln == 0:
                loopRange = 1
            else:
                loopRange = lh - ln + 1


        # Loop through each item in our haystack.
        for i in range(loopRange):
            # Needle is 1 char.
            if ln == 1:
                if haystack[i] == needle:
                    location = i
                    break;
            
            # Needle is larger than 1 char.
            elif haystack[i:i+ln] == needle:
                location = i
                break;

        return location


s = Solution()
t1 = 'aaa'
t1a = 'c'
print(s.strStr('mississippi','pi'))