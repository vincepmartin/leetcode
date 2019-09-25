from datetime import datetime

class Solution:
    def removeVowels(self, S: str) -> str:
        out = ""

        for c in S:
            if c not in ['a','e','i', 'o', 'u']:
                out += c

        return out

    def removeVowels(self, S):
        return ''.join(list(filter(lambda x: x not in ['a','e','i', 'o', 'u'], S)))

s = Solution()

t1 = "xxxaeyiouxyxyz"

then = datetime.now()
print("For loop.")
print(then)
print(s.removeVowels(t1))
print(datetime.now() - then)

then = datetime.now()
print("With Filter.")
print(then)
print(s.removeVowelsWithFilter(t1))
print(datetime.now() - then)
