class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        evens = []
        odds = []
        output = []

        # Split into two containers.
        for i in A:
            if i % 2 == 0:
                evens.append(i)
            else:
                odds.append(i)

        # Evens sorted + Odds sorted.
        for i in sorted(evens):
            output.append(i)
        
        for i in sorted(odds):
            output.append(i)

        return output