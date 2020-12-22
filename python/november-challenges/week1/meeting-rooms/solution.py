# https://leetcode.com/explore/challenge/card/november-leetcoding-challenge/564/week-1-november-1st-november-7th/3515/
from typing import List

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        schedule = {}
        
        for interval in intervals:
            print(interval)
            for i in range(interval[0], interval[1]):
                if i not in schedule:
                    schedule[i] = True
                else:
                    return False

        return True

s = Solution()
print(s.canAttendMeetings([[0,30], [5,10], [15,20]]))
print(s.canAttendMeetings([[1,10], [11,20]]))