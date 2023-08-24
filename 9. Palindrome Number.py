class Solution:
    def isPalindrome(self, x: int) -> bool:
        list1 = list(str(x))
        print(list1)
        list2 = []
        for i in range(len(list1)-1, -1, -1):
            list2.append(list1[i])
        print(list2)
        if list1 != list2:
            return False
        return True
