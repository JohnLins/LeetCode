class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = [[1]]
        for i in range(numRows-1):
            middle = []
            for j in range(len(triangle[-1])-1):
                middle.append(triangle[-1][j] + triangle[-1][j+1])

            temp = [1] + middle + [1]
            triangle.append(temp)

        return triangle
