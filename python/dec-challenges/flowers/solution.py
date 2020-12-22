from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        fblen = len(flowerbed)
        planted = 0 

        # Special case for 1 bed.
        if fblen == 1 and flowerbed[0] == 0:
            planted += 1

        else: 
            # Find a place wherey ou can place a flower.  Place it.
            for i in range(fblen):
                # We have a potential match.
                if flowerbed[i] == 0:
                    # We are not on the edge.
                    if i != 0 and i != fblen - 1:
                        if flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                            flowerbed[i] = 1
                            planted += 1
                    
                    # We are on an edge case.
                    # Begin
                    elif i == 0 and flowerbed[i+1] == 0:
                        flowerbed[i] = 1
                        planted += 1
                    # End
                    elif i == fblen -1 and flowerbed[i-1] == 0:
                        flowerbed[i] = 1
                        planted += 1
            
        if planted >= n:
            return True
        else:
            return False

s = Solution()
t1 = [1,0,0,0,1]
t2 = [0,0,1,0,1]
t3 = [0]

print(s.canPlaceFlowers(t3, 1))