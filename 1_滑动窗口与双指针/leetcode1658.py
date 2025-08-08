from typing import List


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums)
        target = sum(nums) - x
        if target < 0:
            return -1
        ans = -1
        left = 0
        windows = 0
        for right in range(n):
            v = nums[right]
            windows += v  # windows刚开始是一直递增的
            while windows > target:
                windows -= nums[left]
                left += 1
            if windows == target:
                ans = max(ans, right - left + 1)
        return -1 if ans < 0 else n - ans


if __name__ == "__main__":
    a = Solution().minOperations([1, 1, 4, 2, 3], 5)
    print(a)
    a = Solution().minOperations([5, 6, 7, 8, 9], 4)
    print(a)
