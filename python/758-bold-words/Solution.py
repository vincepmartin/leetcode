class Solution:
    def boldWords(self, words, S):
        print("Hello")

    def wordInStringAtN(self, S, n, word):
        match = False
        w = 0
        for i in range(n, n + len(word)):
            print("Testing", S[i], " and ", word[w])
            if word[w] == S[i]:
                match = True
                w += 1
            else:
                return False

        return match

    # return a copy of mask with n '1' inserted at mask[i]
    def newMask(self, mask, i, n):
        newMask = []

        for j in range(0, len(mask)):
            if j >= i and j <= n:
                newMask.append(1)
            else:
                newMask.append(0)

        return newMask
                        
    # insert breaks with mask.
    def applyBRMask(self, S, mask):
        out = ""

        # check first.
        if mask[0] == 1:
            out += "<br>" 

        for i in range(0, len(mask) - 1):
            b = i + 1

            if mask[i] == 1 and mask[b] == 0:
                out += S[i]
                out += "</br>"

            if mask[i] == 0 and mask[b] == 1:
                out += "<br>"
                out += S[i]

            # default lets output the char.
            out += S[i]

        # check last.
        if mask[len(mask)-1] == 1:
            out += S[len(mask)]

        return out

s = Solution()
t1 = "aabcd"

print(s.wordInStringAtN(t1, 0, "ab"))
print(s.wordInStringAtN(t1, 1, "ab"))


tmask = [0,1,1,0,0,1,1,0,0,0]
tstring = "abcdefghik"

print(s.applyBRMask(tstring, tmask))