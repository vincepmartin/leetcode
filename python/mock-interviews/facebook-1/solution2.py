class Solution:
    def customSortString(self, S: str, T: str) -> str:
        sortedOutput = []
        tTemp = list(T)

        for s in S:
            while s in tTemp:
                sortedOutput.append(s)
                tTemp.remove(s)

        return ''.join(sortedOutput) + ''.join(tTemp)            

   
s = Solution()
# s.specialSort("cba", "abc")
# print(s.customSortString("cba", "abcd"))
print(s.customSortString("kqep", "pekeq"), 'should be', "kqeep")




