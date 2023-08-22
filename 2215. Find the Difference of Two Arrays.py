class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        list1 = sorted(nums1)
        list2 = sorted(nums2)
        res = []
        remove_list1 = []
        remove_list2 = []
        for i in range(len(list1)):
            if list1[i] in list2:
                remove_list1.append(list1[i])

        for i in range(len(list2)):
            if list2[i] in list1:
                remove_list2.append(list2[i])

        for i in range(len(remove_list1)):
            list1.remove(remove_list1[i])

        for i in range(len(remove_list2)):
            list2.remove(remove_list2[i])

        list1 = list(set(list1))
        list2 = list(set(list2))

        res.append(list1)
        res.append(list2)

        return(res)
