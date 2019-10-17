class Solution:

    def isValid(self, s: str) -> bool:
        parensPairs = {')':'(', ']':'[', '}':'{'}
        pTemp = []

        # Simple cases for True/False 
        if len(s) == 0:
            return True

        if s[0] in [')', ']', '}'] or len(s) %2 != 0 or len(s) == 0:
            return False

        for p in s:
            print('Eval ', p)
            if p in ['(', '[', '{']:
                pTemp.append(p)
            elif p in [')', ']', '}']:
                # Check to see if this properly closes.
                print(pTemp)
                if pTemp[-1] == parensPairs[p]:
                    pTemp.pop()
                else: # Bail early if this does not properly close.
                    return False

        if len(pTemp) == 0:
            return True

s = Solution()
print(s.isValid('([)]'))