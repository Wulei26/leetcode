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

    def maximumCount(self, nums: List[int]) -> int:
        # 0第一个出现的位置
        zeroPosition = self.lower_bound(nums, 0)
        zeroPosition2 = self.lower_bound(nums, 1)
        # if zeroPosition == zeroPosition2:
        return max(zeroPosition, len(nums) - zeroPosition2)


a = Solution().maximumCount([-2, -1, -1, 1, 2, 3])
print(a)
a = Solution().maximumCount([-3, -2, -1, 0, 0, 1, 2])
print(a)
a = Solution().maximumCount([5, 20, 66, 1314])
print(a)
