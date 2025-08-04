from typing import List


class Solution:
    """
    n == nums.length
    1 <= k <= n <= 105
    -104 <= nums[i] <= 104
    """

    def findMaxAverage(self, nums: List[int], k: int) -> float:
        ans = float("-inf")
        tmp = 0
        for i, v in enumerate(nums):
            tmp += v
            if i < k - 1:
                continue
            ans = max(ans, tmp)
            # 离开窗口
            tmp -= nums[i - k + 1]
        return ans / k


if __name__ == "__main__":
    A = Solution()
    a = A.findMaxAverage([-1, -12, -5, -6, -50, -3], 4)
    print(a)
    a = A.findMaxAverage([-1], 1)
    print(a)
