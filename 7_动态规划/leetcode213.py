from typing import List


class Solution:
    def rob_help(self, nums: List[int]) -> int:
        n = len(nums)
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
    
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        ### 第一个房子偷的情况,那么就不能偷第二个和最后一个了
        case1 = self.rob_help(nums[2:n-1]) + nums[0]
        ### 第一个房子不偷，那么第第二个就可以偷了
        case2 = self.rob_help(nums[1:])
        return max(case1,case2)
if __name__=='__main__':
    a = Solution().rob([2,3,2])