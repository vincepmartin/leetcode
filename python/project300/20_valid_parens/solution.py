class Solution:
    def isValid(self, s: str) -> bool:
        opens = ['(', '[', '{']
        closes = {')':'(', ']':'[', '}':'{'}
        t = []

        # Bail early if we have an odd # of items in s.
        if len(s) % 2 != 0 or len(s) == 0:
            return False

        # We have an even number of items in s.  Process them.
        for c in s:
            if c in opens:
                t.append(c)

            else: # We have a closed item.

                if len(t) != 0 and t[-1] == closes[c]:
                    t.pop()

                else:
                    return False

        # We made it through, a len of 0 left in our temp stack means we had valid parens.
        return len(t) == 0


s = Solution()
t1 = '()'
t2 = '([{}])'
t3 = '([)]'
t4 = ''
t5 = '){'
print(s.isValid(t5))