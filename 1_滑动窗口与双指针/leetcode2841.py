from typing import List
from collections import defaultdict


class Solution:
    """
    1 <= nums.length <= 2 * 104
    1 <= m <= k <= nums.length
    1 <= nums[i] <= 109
    """

    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        n: int = len(nums)
        ans: int = 0
        windows: int = 0  # 长度为k这个窗口的元素和
        tmp: dict = defaultdict(int)  # 记录窗口元素的不重复元素个数
        for i in range(n):
            s = nums[i]
            windows += s
            tmp[s] += 1
            leftp = i - k + 1
            if i < k - 1:
                continue
            # 判断是是否满足 几乎唯一子数组
            if len(tmp) >= m:
                ans = max(windows, ans)
            ##离开窗口
            windows -= nums[leftp]  ##更新窗口和
            tmp[nums[leftp]] -= 1  # 更新元素的出现频次
            if tmp[nums[leftp]] == 0:
                del tmp[nums[leftp]]
        return ans


if __name__ == "__main__":
    a = Solution().maxSum([2, 6, 7, 3, 1, 7], 3, 4)
    print(a)
    a = Solution().maxSum([5, 9, 9, 2, 4, 5, 4], 1, 3)
    print(a)
    a = Solution().maxSum([1, 2, 1, 2, 1, 2, 1], 3, 3)
    print(a)
    a = Solution().maxSum([1, 1, 1, 3], 2, 2)
    print(a)
