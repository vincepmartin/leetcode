class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        evens = []
        odds = []

        for a in A:
            if a % 2 == 0:
                evens.append(a)
            else:
                odds.append(a)

        return evens + odds