class Solution:

    def rotate(self, matrix: List[List[int]]) -> None:


        def shift(top: int, bottom: int, left: int, right: int, r: int):

            if top >= len(matrix)/2:
                return

            for i in range(r-1):


                topleft = [top, left+i]
                topright = [top+i, right]
                bottomright = [bottom, right-i]
                bottomleft = [bottom-i, left]

                temp1 = matrix[topright[0]][topright[1]]
                matrix[topright[0]][topright[1]] = matrix[topleft[0]][topleft[1]]
                temp2 = matrix[bottomright[0]][bottomright[1]]
                matrix[bottomright[0]][bottomright[1]] = temp1
                temp3 = matrix[bottomleft[0]][bottomleft[1]]
                matrix[bottomleft[0]][bottomleft[1]]= temp2
                matrix[topleft[0]][topleft[1]] = temp3

            shift(top+1, bottom-1, left+1, right-1, int(r-2))



        shift(0, len(matrix)-1, 0, len(matrix[0])-1, len(matrix))



        """
        Do not return anything, modify matrix in-place instead.
        """
