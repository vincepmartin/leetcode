class Solution:
    def isValid(self, s: str) -> bool:
        tempList = []
        parens = {'(':')', '[':']', '{':'}'}

        if s == "":
            return True

        # Quick checks, if we have an odd # then we know for sure that it is not valid.
        if len(s)%2 != 0:
            return False

        if s[0] == ')' or s[0] == ']' or s[0] == '}':
            return False

        for c in s:
            if c == '(' or c == '[' or c == '{':
                tempList.append(c)

            elif c == ')' or c == ']' or c == '}':
                # Python has no way to just look at the last item on a list!?
                # Sometimes we have an empty list... So let us check for that first so we don't pop something that doesn't exist...
                if len(tempList) > 0:
                    temp = tempList.pop()
                if parens[temp] != c:
                    tempList.append(temp)

        if len(tempList) == 0:
            return True

        else:
            return False
