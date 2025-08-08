from typing import List


class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        ##最终要将所有的1聚集到一起，那么最后形成的一定是一个长为countOne的子数组，这里的countOne为数组中1的数量
        ##统计有多少1
        n = len(nums)
        countOne = sum(nums)
        if countOne == 0 or countOne == n:
            return 0
        ans = float("inf")
        windows = 0
        for i in range(n + countOne - 1):
            v = nums[i % n]
            if v == 0:
                windows += 1
            if i < countOne - 1:
                continue
            ans = min(ans, windows)
            if nums[i - countOne + 1] == 0:
                windows -= 1
        return ans


if __name__ == "__main__":
    a = Solution().minSwaps([0, 1, 0, 1, 1, 0, 0])
    print(a)
    a = Solution().minSwaps([1, 1, 0, 0, 1])
    print(a)
    a = Solution().minSwaps([0, 0, 0])
    print(a)
