class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums = sorted(nums)
        # print(nums)
        # ave = int(sum(nums) / len(nums))
        # print(ave)
        median = nums[int(len(nums)/2)]
        count = 0
        for i in range(len(nums)):
            if nums[i] >= median:
                count = count + nums[i] - median
            else:
                count = count + median - nums[i]
        return count
        
