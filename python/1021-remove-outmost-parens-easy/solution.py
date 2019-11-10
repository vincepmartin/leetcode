class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        inP = list(S)
        outP = []
        outP.append(inP.pop(0)) 

        while inP:
            firstInP = inP.pop(0)
            if firstInP != outP[-1]:
                outP.append(firstInP)

        return ''.join(outP)

    def removeOuterParentheses2(self, S):
        """
        :type S: str
        :rtype: str
        """

        stack= []
        res = ''
        for i, s in enumerate(S):
                
            if s == ')':
                top = stack.pop()
                if not stack:
                    res += S[pre + 1:i]
            else:  
                if not stack:
                    pre = i
                stack.append(s)  
                
        return res

s = Solution()
tests = ['(()())(())','(()())(())(()(()))', '()()', '(()())(())(()(()x)']
print(f'{tests[-1]} -> {s.removeOuterParentheses2(tests[-1])}')
'''
for t in tests:
    print(f'{t} -> {s.removeOuterParentheses(t)}')
'''