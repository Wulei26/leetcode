class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        ## 也就是有n个台阶需要爬
        ##设dp[i] 为爬 i 个台阶的方案数目
        dp = [0] * (n + 1)
        ##初始化
        dp[1] = 1
        dp[2] = 2
        ## 递推关系，dp[i] = dp[i-1] + dp[i-2]
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]
