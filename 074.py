class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def indexmatrix(i: int) -> int:
            return matrix[int(i/len(matrix[0]))][i-len(matrix[0])*int(i/len(matrix[0]))]


        low = 0
        high = len(matrix[0]) * len(matrix) - 1

        while low <= high:
            i = low + int((high-low)/2)

            v = indexmatrix(i)
            if v == target:
                return True
            if v < target:
                low = i+1
            if v > target:
                high = i-1

        return False
