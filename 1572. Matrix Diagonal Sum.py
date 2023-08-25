class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        count = 0
        for i in range(len(mat)):
            count += mat[i][i]
            print(mat[i][i])
            print(count)

        for i in range(len(mat)):
            count += mat[i][len(mat)-1-i]
            print(mat[i][len(mat)-1-i])
            print(count)

        if len(mat)%2 == 1:
            count = count - mat[len(mat)//2][len(mat)//2]
            # print(count)
        return count
