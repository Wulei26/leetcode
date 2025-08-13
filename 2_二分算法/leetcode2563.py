from typing import List


class Solution:
    def lower_bound(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1
        return left

    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        n = len(nums)
        ans = 0
        for i, v in enumerate(nums):
            ## 对于v先统计左边界
            l = self.lower_bound(nums[0:i], lower - v)
            r = self.lower_bound(nums[0:i], upper - v + 1) - 1
            ans += r - l + 1
        return ans


if __name__ == "__main__":
    a = Solution()
    print(a.countFairPairs([0, 1, 7, 4, 4, 5], 3, 6))
    a = Solution()
