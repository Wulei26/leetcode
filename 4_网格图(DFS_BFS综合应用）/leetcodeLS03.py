from typing import List
class Solution:
    def largestArea(self, grid: List[str]) -> int:
        grid = [list(row) for row in grid]

        if not grid:
            return 0
        m,n = len(grid),len(grid[0])
        ans = 0
        def dfs(i,j,k):
            if i<0 or i>=m or j<0 or j>=n or grid[i][j]=='0':
                return float('-inf')
            if grid[i][j]!=k:
                return 0
            
            grid[i][j] = '7'
            return 1+dfs(i+1,j,k) + dfs(i-1,j,k) + dfs(i,j-1,k) + dfs(i,j+1,k)
        for i in range(m):
            for j in range(n):
                if grid[i][j]!='0' and grid[i][j]!='7':
                    ans = max(ans,dfs(i,j,grid[i][j]))
        return ans

