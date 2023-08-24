import copy

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        origin = list(map(list, matrix))
        for i in range(n):
            for j in range(n):
                matrix[i][j] = origin[n-1-j][i]
                
