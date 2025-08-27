"""
给你一个由 不同 整数组成的数组 nums ，和一个目标整数 target 。请你从 nums 中找出并返回总和为 target 的元素组合的个数。

题目数据保证答案符合 32 位整数范围。
"""

from typing import List
from functools import cache


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        ##本质上还是爬楼梯
        ## 组成target，那么也就是 target - nums[i] 的所有组合数的和
        ###设dp[t] 为组成t 的组合数目
        dp = [0] * (target + 1)

        ## dp[0] = 1 为什么？，因为按照这里的意思，就是什么也不选也算一种方案
        dp[0] = 1
        for i in range(1, target + 1):
            ###组成数字i
            dp[i] = sum(dp[i - x] for x in nums if x <= i)
        return dp[target]
