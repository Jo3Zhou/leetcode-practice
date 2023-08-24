class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        list1 = []
        list1 = nums1 + nums2
        list1 = sorted(list1)
        median_index = len(list1)//2
        print(list1)
        print(median_index)
        if len(list1) == 1:
            return list1[0]
        if len(list1) % 2 == 1:
            return list1[median_index]
        else:
            return (list1[median_index] + list1[median_index-1]) /2
