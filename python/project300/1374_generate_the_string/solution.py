class Solution:
    def generateTheString(self, n: int) -> str:
        # Handle 1:
        if n == 1:
            return 'a'

        # An even string length. 
        if n % 2 == 0:
            return self.makeString(n-1, 'a') + 'b'
        # An odd string length.
        else:
            return self.makeString(n-2, 'a') + 'b' + 'c'
    
    
    def makeString(self, n: int, c: str) -> str:
        return ''.join([c for i in range(n)])

s = Solution()
print(s.generateTheString(4))
print(s.generateTheString(5))
