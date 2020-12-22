from typing import List

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        totals = 0
        songsMap = [0] * 60

        for t in time:
            if t % 60 == 0:
                totals += songsMap[0]
            else:
                totals += songsMap[60 - t % 60]
            
            songsMap[t%60] += 1

        return totals
        '''
        # insane... O(N^2)
        for i in range(len(time)):
            for j in range(len(time)):
                if i != j:
                    if (time[i] + time[j]) % 60 == 0:
                        totals += 1
        return int(totals / 2)
        '''

s = Solution()
t1 = [30,20,150,100,40]
t2 = [60, 60, 60]
t3 = [20, 40]

print(s.numPairsDivisibleBy60(t1))