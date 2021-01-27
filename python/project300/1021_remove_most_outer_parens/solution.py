class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        # If we have an empty string lets just return the same thing.
        if S == '':
            return S

        # A list to store the lists of outer groups.
        og = {}

        # A stack we will use to keep track of our parens.
        ts = []

        # Store our answer.
        ans = []

        # Figure out where the parens we need to remove are located.
        for i in range(len(S)):
            # Check for a begin.
            if len(ts) == 0:
                og[i] =  None
                # og.append(i)

            if S[i] == '(':
                ts.append(S[i])
            else:
                ts.pop()
                # Check for an end.
                if len(ts) == 0:
                    og[i] =  None

        # TODO: Once we have those values return S with those positions removed.
        # This is probably an insanely dumb way to do this...
        # Let's play around with list comprehension for the sake of it...
        # Come back to this... I'm not sure how we can do a list comprehension with indexes... 
        # answer = [S[i] for i in len(S) if i not in og]


        # This might be duplicate work... Perhaps this can be done in the first loop.
        for i in range(len(S)):
            # This might be somewhat expensive... Doing O(P) per O(S)
            # How much faster would it be if we used something like a hash map?
            # This sped it up quite a bit...
            if i not in og:
                ans.append(S[i])

        # This has to be O(N)
        return ''.join(ans)

# Let's test some of this out.
s = Solution()
t1 = '()()'
t2 = '(())'
t3 = '(()())(())'
t4 = '(()())(())(()(()))'

print(s.removeOuterParentheses(t1))
print(s.removeOuterParentheses(t2))
print(s.removeOuterParentheses(t3))
print(s.removeOuterParentheses(t4))