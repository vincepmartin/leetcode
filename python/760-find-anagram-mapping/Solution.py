class Solution(object):
    def anagramMappings(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        
        res = []

        for i in range(0, len(A)):
            for j in range(0, len(B)):
                if A[i] == B[j]:
                    res.append(j)
                    break

        return res

    def anagramMappings2(self, A, B):
        tempB = {}
        res = []

        for i in range(0, len(B)):
            tempB[B[i]] = i

        for j in range(0, len(A)):
            res.append(tempB[A[j]])

        return res


s = Solution()
A = [12, 28, 46, 32, 50]
B = [50, 12, 32, 46, 28]

print(s.anagramMappings(A,B))
print(s.anagramMappings2(A,B))