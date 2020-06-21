class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        # The way i want to do it... return sorted([x*x for x in A])

        for i in range(len(A)):
            A[i] *= A[i]

        A.sort()
        return A