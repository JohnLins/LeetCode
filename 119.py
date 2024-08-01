class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        triangle = [[1]]
        for i in range(1,rowIndex+1):
            middle = []
            for j in range(len(triangle[-1])-1):
                middle.append(triangle[-1][j] + triangle[-1][j+1])

            temp = [1] + middle + [1]
            triangle.append(temp)

        return triangle[-1]
