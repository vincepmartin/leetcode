class Solution:
    def isArmstrong(self, N: int) -> bool:
        aNum = 0
        nList = list(str(N))
        lenN = len(str(N))
        
        for n in nList:
            aNum += pow(int(n),lenN) 
            if aNum > N:
                break

        if aNum != N:
            return False

        else:
            return True