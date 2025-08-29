from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        ## 设置dp [i][j] 为ij到源点的最小和
        dp = [[0] * m for _ in range(n)]
        ###那么第一排和第一列肯定是可以初始化的
        count = 0
        for i in range(m):
            count += grid[0][i]
            dp[0][i] = count
        count = 0
        for i in range(n):
            count += grid[i][0]
            dp[i][0] = count
        ###只能向下或者向右移动，那么一定有
        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

        return dp[n - 1][m - 1]
