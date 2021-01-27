from typing import List

class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums = nums        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        return sum([self.nums[i] * vec.nums[i] for i in range(len(self.nums))])

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)

v1 = SparseVector([1,0,0,2,3])
v2 = SparseVector([0,3,0,4,0])
print(v1.dotProduct(v2))