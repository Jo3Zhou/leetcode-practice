class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        sorted_num = sorted(nums, reverse=True)
        res = sorted_num[k-1]
        return (res)
