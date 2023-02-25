class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        def hourGlass(i , j):
            return grid[i][j] + grid[i -1][j] + grid[i-1][j- 1] + grid[i-1][j + 1] + grid[i + 1][j] + grid[i + 1][j - 1] + grid[i + 1][j + 1]
        
        ans = 0
        for row in range(1, len(grid) -1):
            for col in range(1, len(grid[0]) -1): 
                ans = max(ans , hourGlass( row, col) )

        return ans
                          
        