class Solution:
    def countLetters(self, S: str) -> int:
        i = 0
        total = 0

        i = 0
        j = 0

        while j < len(S):
            if S[i] != S[j]:
                total += self.getCount(j - i)
                i = j
            
            j += 1

        # Wrap it up.
        if i != j:
            total += self.getCount(j - i)

        return total

    # Count single char combos... Ex 3 = 3 + 2 + 1
    def getCount(self, n: int) -> int:
        count = 0
        for i in range(n + 1):
            count += i

        return count

s = Solution()
print(s.countLetters('aaaba'))
print(s.countLetters('a'))