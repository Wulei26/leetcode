from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ## dp[i][j] 是 源点到[i][j]的所有路径总数
        n, m = len(obstacleGrid[0]), len(obstacleGrid)
        dp = [[0] * n for _ in range(m)]
        ##对于第一排，如果遇到0，那么后面全都是0
        for j in range(n):
            if obstacleGrid[0][j] == 1:
                break
            dp[0][j] = 1
        ##对于第一列，如果遇到0，那么后面全都是0
        for i in range(m):
            if obstacleGrid[i][0] == 1:
                break
            dp[i][0] = 1
        ##对于ij，如果为1，那么这个点就是0，如果不是1，那么就是上边和左边的路径和
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]


if __name__ == "__main__":
    obstacleGrid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    a = Solution().uniquePathsWithObstacles(obstacleGrid)
    print(a)
