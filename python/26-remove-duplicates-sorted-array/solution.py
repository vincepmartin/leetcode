class Solution(object):
    def shiftLeft(self, nums, start):
        for i in range(start, len(nums) - 1):
            nums[i] = nums[i + 1]

    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        print(nums)

        # Check for 1 item.
        if len(nums) == 1:
            return 1

        count = 1

        # Shift left until we are OK.
        i = 0
        j = i + 1

        while i < len(nums) - 2:
            if nums[i] == nums[len(nums) - 1]:
                break
            elif nums[i] == nums[i + 1]:
                ### THIS IS TAKING TOO LONG... ### 
                self.shiftLeft(nums, i)
            else:
                i = i + 1
        
        # Figure out the count to return.  
        for i in range(0, len(nums) - 1):
            if nums[i + 1] is not None: 
                if nums[i] != nums[i + 1]:
                    count = count + 1
        
        return count

s = Solution()

test1 = [1, 2]
test2 = [0,0,1,1,1,2,2,3,3,4]

print("test1:")
print(s.removeDuplicates(test1))
print("***")
print("test1:")
print(s.removeDuplicates(test2))
print(test2)
