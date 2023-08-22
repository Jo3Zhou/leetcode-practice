class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1,-1]

        res_list = []
        count = nums.count(target)
        index = nums.index(target)
        res_list.append(index)
        res_list.append(index + count - 1)

        return(res_list)
