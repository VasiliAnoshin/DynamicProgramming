class Solution:
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

sol = Solution()
print(sol.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,-1]]))
print(sol.uniquePathsWithObstacles([[0],[0]]))
print(sol.uniquePathsWithObstacles([[1,0]]))
print(sol.uniquePathsWithObstacles([[0,0,0,0,0],[0,0,0,0,1],[0,0,0,1,0],[0,0,1,0,0]]))