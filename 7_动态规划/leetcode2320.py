class Solution:
    def countHousePlacements(self, n: int) -> int:
        MOD = 10 **9 + 7
        ## 设dp[i]为 i个地块可以放置的房子数，两边相互独立
        dp = [0]* (n + 1)
        ##第i个地块可以选择放或者不放
        ## 不放，那么方案数就是dp[i-1]
        #放，那么i-1处就不能放置了 方案为dp[i-2]
        dp[1] = 2
        if n == 1: return 4
        dp[2] = 3
        for i in range(3,n + 1):
            dp[i] = dp[i-1] + dp[i-2]
        ##两个街道独立
        return dp[n] ** 2 % MOD