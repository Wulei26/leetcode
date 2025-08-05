from typing import List


class Solution:
    """
    n == nums.length
    1 <= n <= 105
    0 <= nums[i], k <= 105"""

    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if k * 2 + 1 < n:
            return [-1] * n
        if k == 0:
            return nums
        ans = []
        tmp = 0
        for i in range(n - k):
            v = nums[i]
            tmp += v
            if i < k * 2 + 1:
                continue
            ans.append(int(tmp / (k * 2 + 1)))
            # 移除窗口
            tmp -= nums[i - k * 2 - 1]
        return [-1] * k + ans + [-1] * k


if __name__ == "__main__":
    a = Solution().getAverages([7, 4, 3, 9, 1, 8, 5, 2, 6], 3)
    print(a)
