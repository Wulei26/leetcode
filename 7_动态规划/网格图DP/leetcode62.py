class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ## dp[i][j] 是 源点到[i][j]的所有路径总数
        dp = [[0] * n for _ in range(m)]
        ##第一排肯定是1，因为只能从右边过来达到
        for i in range(n):
            dp[0][i] = 1
        ##第一列肯定也是1，只能从上边过来
        for i in range(m):
            dp[i][0] = 1
        ##对于ij只能是从上面或者左边过来，那么就是二者之和
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]
