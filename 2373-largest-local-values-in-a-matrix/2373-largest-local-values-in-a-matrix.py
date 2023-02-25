class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        
        ans =  [[0] * (n - 2) for _ in range(n - 2)]
        for row in range(n - 2):
            for col in range(n - 2):
                ans[row][col] = max(grid[row][col], grid[row][col + 1], grid[row][col + 2],
                                    grid[row + 1][col], grid[row + 1][col + 1], grid[row + 1][col + 2],
                                    grid[row + 2][col], grid[row + 2][col + 1], grid[row + 2][col + 2] )
        return ans