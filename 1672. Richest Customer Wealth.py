class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        list1 = []
        for c in accounts:
            list1.append(sum(c))
        print(list1)
        return max(list1)
