class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zeros = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    zeros.append([i,j])

        for z in zeros:
            for i in range(0,len(matrix)):
                matrix[i][z[1]] = 0

            for i in range(0,len(matrix[0])):
                matrix[z[0]][i] = 0
