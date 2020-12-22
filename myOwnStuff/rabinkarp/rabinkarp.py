from typing import str
from ..linkedlist import LinkedList

class RabinKarp:
    def __init__(self, subString: str, bigString: str):
        # Some error checking.
        if len(subString) > len(bigString):
            raise Exception('subString is larger than bigString')

        elif len(subString) == 0 or len(bigString) == 0:
            raise Exception('0 len string provided.')
        
        # We seem to havemade it...
        self.subString = subString
        self.bigString = bigString

        # We are going to need a rolling hash.
                 
