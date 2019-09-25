class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # Don't even bother with negs.
        if nums < 0:
            return

        # I think this op is O(n)
        temp = list(nums)

        # This op is O(N) as well
        for i in range(0, len(nums)):
            nums[(i + k) % len(temp)] = temp[i]

t1 = [1,2,3,4,5,6,7]
k1 = 3
s = Solution()
s.rotate(t1,k1)
print(t1)