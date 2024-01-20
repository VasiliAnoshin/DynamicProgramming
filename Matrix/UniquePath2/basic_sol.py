class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if obstacleGrid[m-1][n-1]:
            return 0
        tmp = obstacleGrid[-1]
        for idx in range(len(tmp)-1, -1, -1):
            if idx+1 < n and obstacleGrid[-1][idx+1] == -1:
                tmp[idx] = -1
            elif obstacleGrid[-1][idx] == 0: 
                tmp[idx] = 1
            elif obstacleGrid[-1][idx] == 1:
                tmp[idx] = -1
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

sol = Solution()
print(sol.uniquePathsWithObstacles([[0],[0]]))
print(sol.uniquePathsWithObstacles([[1,0]]))
print(sol.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))
print(sol.uniquePathsWithObstacles([[0,0,0,0,0],[0,0,0,0,1],[0,0,0,1,0],[0,0,1,0,0]]))
