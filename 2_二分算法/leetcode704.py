from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1
        if left == len(nums):
            return -1
        if nums[left] == target:
            return left
        return -1


if __name__ == "__main__":
    nums = [0, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5, 9, 100, 120]
    a = Solution()
