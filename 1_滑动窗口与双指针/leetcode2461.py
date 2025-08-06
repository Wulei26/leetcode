from typing import List
from collections import defaultdict


class Solution:
    """
    1 <= k <= nums.length <= 105
    1 <= nums[i] <= 105"""

    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        windows = 0
        dct = defaultdict(int)
        for i in range(n):
            s = nums[i]
            leftp = i - k + 1
            windows += s
            dct[s] += 1
            if i < k - 1:
                continue
            # 判断是否满足
            if len(dct) == k:
                ans = max(ans, windows)
            ## 离开windows
            windows -= nums[leftp]
            dct[nums[leftp]] -= 1
            if dct[nums[leftp]] == 0:
                del dct[nums[leftp]]
        return ans


if __name__ == "__main__":
    a = Solution().maximumSubarraySum([1, 5, 4, 2, 9, 9, 9], 3)
    print(a)
