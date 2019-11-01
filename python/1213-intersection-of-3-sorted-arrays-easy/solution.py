class Solution:
    # Dumbest way possible...
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        # Convert all to a set? Combine only the ones that are similar?
        # Do an intersection
        return sorted(list(set(arr1) & set(arr2) & set(arr3)))