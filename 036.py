class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            rownums = set()
            for j in range(9):
                x = board[i][j]
                if x in rownums and x != ".":
                    return False

                rownums.add(x)

        for i in range(9):

            colnums = set()
            for j in range(9):
                x = board[j][i]
                if x in colnums and x != ".":

                    return False

                colnums.add(x)


        for i in range(3):
            for j in range(3):
                squarenums = set()
                for k in range(3):
                    for p in range(3):
                        x = board[3*j+k][3*i+p]
                        if x in squarenums and x != ".":
                            return False
                        squarenums.add(x)


        return True
