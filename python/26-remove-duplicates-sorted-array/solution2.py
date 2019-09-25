class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]

        return i + 1

s = Solution()

test1 = [1, 2]
test2 = [0,0,1,1,1,2,2,3,3,4]

print("test1:")
print(s.removeDuplicates(test1))
print("***")
print("test1:")
print(s.removeDuplicates(test2))
print(test2)
