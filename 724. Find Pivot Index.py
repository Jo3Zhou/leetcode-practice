class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            left_sum = sum(nums[:i])
            right_sum = sum(nums[i+1:])
            # print(f'index = {i}, left_sum = {left_sum}, right_sum = {right_sum}')
            if left_sum == right_sum:
                return (i)
        return(-1)
