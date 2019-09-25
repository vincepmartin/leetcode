class Solution(object):
    def toLowerCase(self, s):
        """
        :type str: str
        :rtype: str
        """

        out = []

        for c in s:
            if ord(c) >= 65 and ord(c) <= 90:
                out.append(chr(ord(c) + 32))
            else:
                out.append(c)
        
        return ''.join(out) 
        
        