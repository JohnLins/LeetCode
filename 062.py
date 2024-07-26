class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        if n == 1 and m == 1:
            return 1

        grid = []
        for i in range(m):
            grid.append([])
            for j in range(n):
                grid[i].append(0)


        for i in range(m-1, -1,-1):
            for j in range(n-1, -1,-1):
                below = 0
                if i+1 < len(grid):
                    below = grid[i+1][j]
                right = 0
                if j+1 < len(grid[0]):
                    right = grid[i][j+1]
                x = below + right
                if i == m-1:
                    x = 1
                grid[i][j] = x


        below = 0
        if 1 < len(grid):
            below = grid[1][0]
        right = 0
        if 1 < len(grid[0]):
            right = grid[0][1]

        return below + right
