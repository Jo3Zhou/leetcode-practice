class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        list1 = []
        for l in matrix:
            list1 = list1 + l
        print(list1)
        if target in list1:
            return True
        else:
            return False
