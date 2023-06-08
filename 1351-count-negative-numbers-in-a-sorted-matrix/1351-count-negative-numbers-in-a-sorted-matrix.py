class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        ans = 0
        m = len(grid)
        n = len(grid[0])
        
        for i in range(m):
            if i < 0:
                ans += (m - i) * n
                break
            for j in range(n):
                if grid[i][j] < 0:
                    ans += (n - j)
                    break
        
        return ans