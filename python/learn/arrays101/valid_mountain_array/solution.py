from typing import List

class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        last = A[0]
        positiveInflectionPoint = None
        negativeInflectionPoint = None

        ips = {}
         
        s = 0 
        oldS = 0 
       
        for i in range(1, len(A)):
            # Calculate the slope.
            oldS = s 
            s = A[i] - A[i - 1]
            
            print(f"Slope is: {s} between {i} and {i - 1}")

            # The same.
            if s == oldS:
                print("Slope are the same")
                return False

            # Increase
            if s > 0 and oldS > 0:
                print("** Slope is increasing!")
                print("No inflection point")

            # Decrease
            if s < 0 and oldS < 0:
                print("Slope is decreasing!")
                print("No inflection point")
                
            # Same
            else:
                print(f"Inflection point found at {i}")
                if s < oldS and positiveInflectionPoint == None:
                    print("Negative inflection point.")
                    print("Not a mountain, lacks positive climb.") 
                    return False

                elif s > oldS:
                    print("Positive inflection point.")
                    positiveInflectionPoint = i

 
                   print("Not a mountain, lacks negative fall.")
                    return False

        if negativeInflectionPoint == None or positiveInflectionPoint == None:
            return False

        return True

s = Solution()
t1 = [2,1]
t1s = False

t2 = [3,5,5]
t2s = False

t3 = [0, 3, 2, 1]
t3s = True

print(f" {t1} is {s.validMountainArray(t1)}")
print("*****")
print(f" {t2} is {s.validMountainArray(t2)}")
print("*****")
print(f" {t3} is {s.validMountainArray(t3)}")