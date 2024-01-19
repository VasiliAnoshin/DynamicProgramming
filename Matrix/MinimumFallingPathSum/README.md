```python
class Solution:
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        for row in range(rows-2, -1,-1):
            for col in range(cols):
                tmp = []
                if row+1 < rows and col + 1 < cols:
                    tmp.append(matrix[row+1][col+1])
                if row+1 < rows:
                    tmp.append(matrix[row+1][col])
                if col-1 >=0:
                    tmp.append(matrix[row+1][col-1])
                matrix[row][col] = matrix[row][col] + min(tmp)
        return min(matrix[0])
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>)