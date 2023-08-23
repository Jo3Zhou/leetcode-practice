class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if nums.index(max(nums)) == 0:
            return 0
        if nums.index(max(nums)) == len(nums)-1:
            return len(nums)-1

        for i in range(1, len(nums)-1):
            if nums[i] > nums[i-1] and nums[i] >= nums[i+1]:
                return i
