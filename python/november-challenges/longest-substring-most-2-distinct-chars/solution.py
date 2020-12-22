
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        # Defined by the problem.
        maxDistinctAllowed = 2

        # Temp store the individual char count.  Used to check if we are over maxDistinctAllowed.
        distinctMap = {}
        distinctStringLength = 0
        maxDistinctStringLength = 0

        # Really bad, probably O(N^2)
        for i in range(len(s)):
            distinctStringLength = 0
            distinctMap = {}
            for j in range(i, len(s)):
                if s[j] not in distinctMap:
                    distinctMap[s[j]] = None

                if len(distinctMap) > maxDistinctAllowed:
                    break;
                
                distinctStringLength += 1
            
            if distinctStringLength > maxDistinctStringLength:
                maxDistinctStringLength = distinctStringLength

        return maxDistinctStringLength 

s = Solution()

t1 = 'eceba'
t2 = 'ccaabbb'
print(s.lengthOfLongestSubstringTwoDistinct(t1))
print(s.lengthOfLongestSubstringTwoDistinct(t2))