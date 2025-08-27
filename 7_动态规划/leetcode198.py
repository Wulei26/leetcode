from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0: return 0
        if n == 1: return nums[0]
        ### 设 dp[k] 为偷盗 前1:k个房子的最大价值
        dp = [0] * (n + 1)

        ##k = 1 ，只有一个房子，那必须偷了
        dp[1] = nums[0]
        ##如果有两间房子，偷大的那个
        dp[2] = max(nums[0], nums[1])
        ###如果有三个以上的房子，那么使用递推关系
        ## 第k个房子到底偷不偷，如果前面一个房子偷了，那么就不能了 金额为 dp[k - 1]
        #### 如果前面一个房子没偷，那么就偷这个 dp[k-2] + nums[k]

        for k in range(3,n + 1):
            dp[k] = max(dp[k-1], dp[k-2] + nums[k-1])
        return dp[n]
if __name__=='__main__':
    a = Solution().rob([2,7,9,3,1])
    print(a)