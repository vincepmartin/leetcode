class Solution(object):
    def mergeSort(self, nums):
        if len(nums) > 1:
            mid = len(nums)//2
            L = nums[:mid]
            R = nums[mid:]

            self.mergeSort(L)
            self.mergeSort(R)

            i = j = k = 0
            
            #
            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    nums[k] = L[i]
                    i += 1
                    k += 1
                else:
                    nums[k] = R[j]
                    j += 1
                    k += 1

            while i < len(L):
                nums[k] = L[i]
                i += 1
                k += 1

            while j < len(R):
                nums[k] = R[j]
                j += 1
                k += 1

   
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # Put everything into one array.
        j = 0
        for i in range(m, m+n):
            nums1[i] = nums2[j]
            j += 1

        # Sort that array.
        self.mergeSort(nums1)

s = Solution()
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

print("nums1: ", nums1, " nums2: ", nums2)
s.merge(nums1,m,nums2,n)
print nums1   