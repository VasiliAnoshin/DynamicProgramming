``` python
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        # Check if its worth to check all possibilities. 
        # If findal destination != 1. There is no valid path
        if obstacleGrid[m-1][n-1]:
            return 0
        # Caclulate last_row. Based on this row calculate rest of solution.
        tmp = [0] * n
        for idx in range(len(tmp)-1, -1, -1):
            if idx+1 < n and obstacleGrid[-1][idx+1] == -1:
                tmp[idx] = -1
            elif obstacleGrid[-1][idx] == 0: 
                tmp[idx] = 1
            elif obstacleGrid[-1][idx] == 1:
                tmp[idx] = -1
        # Calculate rest of the rows. Check if cur position is not obstacle. 
        # And then add number of ways to calc the right way.
        for i in range(m-2, -1, -1):
            new_row = [1] * n
            for j in range(n-1, -1, -1):
                if obstacleGrid[i][j]:
                    new_row[j] = -1
                    continue
                cnt = 0
                if  (j+1<n and new_row[j+1] != -1):
                    cnt = new_row[j+1]
                if  tmp[j] != -1:
                    cnt += tmp[j]
                new_row[j] = cnt
            tmp = new_row
        return 0 if tmp[0] == -1 else tmp[0]
```

Explanation: 
1) Calculate last row include obstacles.
2) Calculate rest of the rows based on prev calculated row.

SMART: 
``` python
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [0] *n
        dp[n-1] = 1
        for r in reversed(range(m)):
            for c in reversed(range(n)):
                if obstacleGrid[r][c]:
                    dp[c] = 0
                elif c+1 < n:
                    dp[c] = dp[c] + dp[c+1]
        return dp[0]
```