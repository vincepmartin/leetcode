class Solution:
    def defangIPaddr(self, address: str) -> str:
        rVal = ''
        blocks = 0 
        for n in address.split('.'):
            rVal += n
            if blocks < 3:
                rVal += '[.]'
                blocks += 1

        return rVal