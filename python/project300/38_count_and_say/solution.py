class Solution:
    def countAndSay(self, n:int):
        if n == 0:
            return 0

        ans = '1'
        for ni in range(1, n):
            ans = self.say(ans)
            #print(f'ni: {ni} say: {ans}')

        return ans


    # parse a number -> string into a speak and say string.
    def say(self, n: str) -> str:
        t = [] # Store intermediate answer.
        ans = [] # Store combination of all initermediate answers.
        for i in n:
            if i in t or len(t) == 0:
                t.append(i)
            
            else:
                ans.append(str(len(t))) # Our count.
                ans.append(t[0]) # Our actual number.
                t = [i]


        # check the last item.
        ans.append(str(len(t)))
        ans.append(t[0])

        return ''.join(ans)

# Testing.
s = Solution()
print(s.countAndSay(0))
print(s.countAndSay(1))
print(s.countAndSay(4))