class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        list1 = sorted(nums, reverse=True)
        list2 = sorted(nums, reverse=False)
        if nums != list1 and nums != list2:
            return False
        return True
