class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        list1 = nums1[:3]
        list2 = nums2[-3:]

        res_list = list1 + list2
        nums1 = sorted(res_list)
