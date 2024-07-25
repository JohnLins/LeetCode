class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def search(x: int, y: int, i: int, path):

            p = path.copy()

            i += 1
            p.append((x,y))


            if i == len(word):
                return True


            b = False

            if y+1 <= len(board[0])-1 and (x,y+1) not in p and word[i]==board[x][y+1]:
                b = b or search(x, y+1, i, p)

            if x+1 <= len(board)-1 and (x+1,y) not in p and word[i]==board[x+1][y]:
                b = b or search(x+1, y, i, p)

            if y-1 >= 0 and (x,y-1) not in p and word[i]==board[x][y-1]:
                b = b or search(x, y-1, i, p)

            if x-1 >= 0 and (x-1,y) not in p and word[i]==board[x-1][y]:
                b = b or search(x-1, y, i, p)




            return b



        for i in range(len(board)):
            for j in range(len(board[0])):

                if board[i][j] == word[0]:
                    s = search(i,j,0,[])
                    if s == True:
                        return True


        return False








