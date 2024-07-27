class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        path = [(0,0)]
        values = [matrix[0][0]]
        i=0
        j=0
        m = len(matrix)
        n = len(matrix[0])
        direction = "right"


        while len(values) < (n*m):


            if j+1 <= n-1 and (i,j+1) not in path and direction == "right":
                j+=1


                path.append((i,j))
                values.append(matrix[i][j])
                continue




            if i+1 <= m-1 and (i+1, j) not in path and direction == "down":
                i+=1

                path.append((i,j))
                values.append(matrix[i][j])

                continue



            if j-1 >= 0 and (i, j-1) not in path and direction == "left":
                j-=1

                path.append((i,j))
                values.append(matrix[i][j])

                continue




            if i-1 >= 0 and (i-1, j) not in path and direction == "up":
                i-=1

                path.append((i,j))
                values.append(matrix[i][j])

                continue



            if direction == "right":
                direction = "down"
            elif direction == "down":
                direction = "left"
            elif direction == "left":
                direction = "up"
            elif direction == "up":
                direction = "right"




        return values
