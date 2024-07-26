class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid[0])
        m = len(obstacleGrid)
        if obstacleGrid[0][0] == 1:
            return 0

        if n == 1 and m == 1:
            return 1


        grid = []
        for i in range(m):
            grid.append([])
            for j in range(n):
                grid[i].append(0)

        grid[m-1][n-1] = 1
        for i in range(m-1, -1,-1):
            for j in range(n-1, -1,-1):
                below = 0
                if i+1 < len(grid) and obstacleGrid[i+1][j] != 1:
                    below = grid[i+1][j]
                right = 0
                if j+1 < len(grid[0]) and obstacleGrid[i][j+1] != 1:
                    right = grid[i][j+1]
                x = below + right
                if i != m-1 or j != n-1:
                    grid[i][j] = x



        below = 0
        if 1 < len(grid) and obstacleGrid[1][0] != 1:
            below = grid[1][0]
        right = 0
        if 1 < len(grid[0]) and obstacleGrid[0][1] != 1:
            right = grid[0][1]

        return below + right
