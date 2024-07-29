class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        word1 = " " + word1
        word2 = " " + word2
        grid = []
        for i in range(len(word2)):
            row = []
            for j in range(len(word1)):
                if i == 0:
                    row.append(j)
                elif j == 0:
                    row.append(i)
                else:
                    above = grid[i-1][j]
                    left = row[j-1]
                    topleft = grid[i-1][j-1]
                    if word1[j] != word2[i]:
                        row.append(min(min(above, left), topleft)+1)
                    else:
                        row.append(topleft)
            grid.append(row)


        return grid[-1][-1]
