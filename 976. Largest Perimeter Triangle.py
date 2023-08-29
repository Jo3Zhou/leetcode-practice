class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums = sorted(nums, reverse=True)
        print(nums)
        perimeter = 0
        for i in range(len(nums)-2):
            if nums[i+1] + nums[i+2] > nums[i]:
                return nums[i+1] + nums[i+2] + nums[i]

        if perimeter == 0:
            return 0
