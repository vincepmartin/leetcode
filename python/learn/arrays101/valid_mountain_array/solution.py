from typing import List

class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        # Sometimes we are given something with only one value. 
        if not A or len(A) == 1:
            return False

        ips = []
        iCount = 0
        s = 0 
        oldS = 0 
            
        for i in range(1, len(A)):
            # Calculate the slope.
            oldS = s 
            s = A[i] - A[i - 1]
            
            print(f"Slope is: {s} between {i} and {i - 1}")

            # The same.
            if s == 0:
                print("Slope are the same")
                return False

            # Increase
            elif s > 0 and oldS > 0:
                print("** Slope is increasing!")
                print("No inflection point")

            # Decrease
            elif s < 0 and oldS < 0:
                print("Slope is decreasing!")
                print("No inflection point")
                
            # Inflection point detected 
            else:
                print(f"Inflection point found at {i}")
                iCount += 1

                if s > oldS:
                    ips.append(1)
                
                else:
                    if not ips:
                        return False
                    else:
                        ips.pop()

        print(f"count: {iCount}")
        
        if iCount == 2 and not ips:
            print("***** RETURNING TRUE *****")
            return True

        else:
            return False

s = Solution()
'''
t1 = [2,1]
t1s = False

t2 = [3,5,5]
t2s = False
'''

t3 = [0, 3, 2, 1]
t3s = True

t4 = [3,7,6,4,3,0,1,0]
t4s = False

t5 = [0,1,2,4,2,1]
t5s = True

print(f" {t3} is {s.validMountainArray(t3)}")
print(f" {t5} is {s.validMountainArray(t5)}")