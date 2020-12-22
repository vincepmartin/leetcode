from typing import List, Tuple
class Solution:
    x = 0
    y = 0
    m = None
    directions = ['right', 'down', 'left', 'up']
    currentDir = 0

    def generateMatrix(self, n: int) -> List[List[int]]:
        # Create an empty matrix to fill up.
        self.createEmptyMatrix(n)

        # Travel the matrix in a spiral.
        for i in range(1, n*n + 1):
            # Place our current num into matrix.
            self.m[self.y][self.x] = i

            # If move is not OK Move then change directions.
            if not self.moveOK(n):
                if self.currentDir < len(self.directions) - 1:
                    self.currentDir += 1
                else:
                    self.currentDir = 0

            # Move.
            self.x, self.y = self.moveCoords(self.directions[self.currentDir])

        return self.m

    def createEmptyMatrix(self, n):
        self.m = []
        for x in range(n):
            self.m.append([None] * n)

    def moveOK(self, n: int) -> bool:
        newX, newY = self.moveCoords(self.directions[self.currentDir])
        
        # Are we out of bounds?
        if newX > n-1 or newX < 0 or newY > n-1 or newY < 0:
            return False
        
        # Does our proposed direction cause any collisions?
        if self.m[newY][newX] == None:
            return True

        return False


    def moveCoords(self, direction: str) -> Tuple[int, int]:
        if direction == 'right':
            return self.x+1, self.y
        elif direction == 'down':
            return self.x, self.y+1
        elif direction == 'left':
            return self.x-1, self.y
        elif direction == 'up':
            return self.x, self.y-1

s = Solution()
t1 = 4 

for i in s.generateMatrix(t1):
    print(i)