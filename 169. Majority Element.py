class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        list1 = list(set(nums))
        list_ = []
        for i in list1:
            list_.append([nums.count(i), i])
        list_ = sorted(list_, key=lambda x:x[0], reverse=True)
        print(list_)
        return list_[0][1]
