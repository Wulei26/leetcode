from typing import List


class Solution:
    def lower_bound(self, nums: List[int], target: int) -> int:
        ##在num[i] <= nums[i+1]的数组中，返回满足 target <= nums[i] 的最小的i
        # 数组为空的话，或者所有的值都小于 target ，那么则返回 len(nums)
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (right + left) // 2
            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1
        return left

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = self.lower_bound(nums, target)
        if start == len(nums) or nums[start] != target:
            return [-1, -1]
        end = self.lower_bound(nums, target + 1) - 1
        return [start, end]


if __name__ == "__main__":
    nums = [0, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5, 9, 100, 120]
    a = Solution()
    print(a.lower_bound(nums, 130))
    print(len(nums))
