from typing import List
class Solution:
    def dfs(self, grid: List[list[int]], i: int, j: int):
        ##将 数字为1的地方上下左右 为1的地方全部变成2
        if i < 0 or i > len(grid[0]) or j <0 or j >= len(grid) or grid[i][j] == '2' or grid[i][j] == '0':
            return
        grid[i][j] = '2'
        self.dfs(grid,i,j-1)
        self.dfs(grid,i,j + 1)
        self.dfs(grid,i-1,j)
        self.dfs(grid,i+1,j)
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    count += 1
        return count

if __name__=='__main__':
    grid = [
            ["1","1","1","1","0"],
            ["1","1","0","1","0"],
            ["1","1","0","0","0"],
            ["0","0","0","0","0"]
            ]
    a = Solution()
    print(a.numIslands(grid))