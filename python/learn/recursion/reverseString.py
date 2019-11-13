from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        self.helper(s, 0, len(s) - 1)

    # Fucked up version that does len(s) calls.
    '''
    def helper(self, w, i):
        # Base case.
        if i == len(w):
            return
        
        else:
            self.helper(w, i + 1)
            if i >= len(w) / 2:
                print(f'Swapping {i} and {len(w) -1 - i}')
                w[i], w[len(w) -1 - i] = w[len(w) -1 - i], w[i] 
    '''

    # We can do this in len(s)/2 calls if we use 2 pointers.  One that starts at the begining
    # array and one that starts at the end.  Counting forward and backwards with a base case of 
    # left = right.
    def helper(self, s, left, right):
        # Base case where our pointers are in the same place.
        if left >= right:
            return

        else:
            self.helper(s, left + 1, right - 1)
            s[left], s[right] = s[right], s[left] 


s = Solution()
t1 = ['d','o','g']
t2 = ['a','b','c', 'd']
t3 = ['h','e','l', 'l', 'o']

for x in [t1, t2, t3]:
    print(str(x))
    s.reverseString(x)
    print(str(x))