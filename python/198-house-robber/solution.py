class Solution:
    
    def rob(self, nums):
        
        last, now = 0, 0
        
        for i in nums: last, now = now, max(last + i, now)
                
        return now
s = Solution()
t1 = [2,7,9,3,1]
t2 = [1,2,3,1]
t3 = [1, 1, 1]
t4 = [2,3,2]
print(s.rob(t4))