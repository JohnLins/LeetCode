class Solution:
    def helper(self, x, y, total, store, grid):
            if x == len(grid)-1 and y == len(grid[0])-1:
                return total + grid[x][y]

            s = -1
            if (x,y) in store:
                return store[(x,y)] + total

            if x + 1 < len(grid) and y+1 < len(grid[0]):
                s = min(self.helper(x+1,y, total + grid[x][y], store, grid) ,
                self.helper(x,y+1, total + grid[x][y], store, grid))

            elif x+1 < len(grid):
                s = self.helper(x+1, y, total + grid[x][y], store, grid)

            elif y+1 < len(grid[0]):
                s = self.helper(x, y+1, total + grid[x][y], store, grid)

            store[(x,y)] = s - total

            return s

    def minPathSum(self, grid: List[List[int]]) -> int:
        store = {}

        return self.helper(0 , 0, 0, store, grid)

