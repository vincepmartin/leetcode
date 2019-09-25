class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        counts = {}
        maxElement = None

        for e in nums:
            if e in counts:
                counts[e] = counts[e] + 1
                if maxElement == None:
                    maxElement = e

            else:
                counts[e] = 1
                if maxElement == None:
                    maxElement = e

            if counts[e] > counts[maxElement]:
                maxElement = e

        return maxElement

s = Solution()
t1 = [3,2,3]

print(s.majorityElement(t1))