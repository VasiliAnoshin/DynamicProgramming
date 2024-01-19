class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        rows = len(triangle)
        cols = len(triangle[0])
        for i in range(rows-2, -1, -1):
            for j in range(len(triangle[i])):
                triangle[i][j] = triangle[i][j] + min(triangle[i+1][j], triangle[i+1][j+1])
        return triangle[0][0]
sol = Solution()
sol.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]])