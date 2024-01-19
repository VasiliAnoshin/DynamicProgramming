```python
    class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        rows = len(triangle)
        for i in range(rows-2, -1, -1):
            for j in range(len(triangle[i])):
                triangle[i][j] = triangle[i][j] + min(triangle[i+1][j], triangle[i+1][j+1])
        return triangle[0][0]
```

Time Complexity: ![O(n^2)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>)