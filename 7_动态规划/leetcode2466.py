class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        ###本质还是爬楼梯，每次 添加 zero 个0 或者one个1
        ### 也就是每次只能爬 zero 或者 one 个台阶，问 爬行 low 个台阶的 方案数目
        # dp[i] 为 组成长度为i的字符串的方案数目
        MOD = 10**9 + 7
        dp = [0] * (high + 1)
        dp[0] = 1

        for i in range(1, high + 1):
            count = 0
            if i >= zero:
                ##相当于在结尾添加一zero个0
                count = count + dp[i - zero]
            if i >= one:
                count = count + dp[i - one]
            dp[i] = count
        return sum(dp[low:]) % MOD
