from typing import List
import math

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        unitPerSecond = 1
        totalDistance = 0
        current = []

        for p in range(0, len(points) - 1):
            current = points[p]
            print(f'Set initial point to {current}')
            # Move diag until we are on the same X or Y plane.
            while current[0] != points[p + 1][0] or current[1] != points[p + 1][1]:
                current = self.moveDiag1Towards(current, points[p+1])
                print(f'Moved to {current}')

            

        timeTraveled = totalDistance * unitPerSecond 
        return timeTraveled

    def moveDiag1Towards(self, pointA, pointB) -> List[int]:
        # New
        newPos = pointA

        # Positive X movement and positive Y
        if pointB[0] - pointA[0] > 0 and pointB[1] - pointA[1] > 0:
           newPos[0] += 1
           newPos[1] += 1

        # Positive X movement and negative Y
        elif pointB[0] - pointA[0] > 0 and pointB[1] - pointA[1] < 0:
           newPos[0] += 1
           newPos[1] -= 1

        # Negative X movement and positive Y
        elif pointB[0] - pointA[0] < 0 and pointB[1] - pointA[1] > 0:
           newPos[0] -= 1
           newPos[1] += 1

        # Negative X movement and negative Y
        elif pointB[0] - pointA[0] < 0 and pointB[1] - pointA[1] < 0:
           newPos[0] -= 1
           newPos[1] -= 1

        print(f'Moving from {pointA} to {newPos}')
        return newPos

    def distance(self, pointA: List[int], pointB: List[int]) -> int:
        return math.floor(math.sqrt(pow(pointA[0] - pointB[0], 2) + pow(pointA[1] - pointB[1], 2)))

s = Solution()
t1 = [[1,1],[3,4],[-1,0]]
print(s.minTimeToVisitAllPoints(t1))