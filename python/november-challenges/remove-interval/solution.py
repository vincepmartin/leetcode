class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        # I think we should go through each interval and simplify it.
        # Example is.
        # [[0, 4],[6,10],[11,20]] => [[0,4],[6,20]]

        simplifiedIntervals = []

        for i in intervals:
            # if we have nothing in the list add.
            if len(simplifiedIntervals) == 0:
                simplifiedIntervals.push(i)

            # check if we should go before.
            elif i[1]
            # check if we should go after.

            # merge into list.

        pass