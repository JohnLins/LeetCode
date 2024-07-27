class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        print("Hey:")
        matrix = []
        for k in range(n):
            matrix.append([])
            for h in range(n):
                matrix[k].append(0)


        print(matrix)
        path = [(0,0)]

        i=0
        j=0

        direction = "right"
        value = 1
        matrix[0][0]=value
        while value < (n*n):
            print(value)

            if j+1 <= n-1 and (i,j+1) not in path and direction == "right":
                j+=1


                path.append((i,j))
                value+=1
                matrix[i][j] = value

                continue




            if i+1 <= n-1 and (i+1, j) not in path and direction == "down":
                i+=1

                path.append((i,j))
                value+=1
                matrix[i][j] = value

                continue



            if j-1 >= 0 and (i, j-1) not in path and direction == "left":
                j-=1

                path.append((i,j))
                value+=1
                matrix[i][j] = value

                continue




            if i-1 >= 0 and (i-1, j) not in path and direction == "up":
                i-=1

                path.append((i,j))
                value+=1
                matrix[i][j] = value

                continue



            if direction == "right":
                direction = "down"
            elif direction == "down":
                direction = "left"
            elif direction == "left":
                direction = "up"
            elif direction == "up":
                direction = "right"




        return matrix
