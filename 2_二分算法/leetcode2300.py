from typing import List


class Solution:
    def lower_bond(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1
        return left

    def successfulPairs(
        self, spells: List[int], potions: List[int], success: int
    ) -> List[int]:
        ##先将potions进行排序
        n, m = len(spells), len(potions)
        ans = [0] * n
        potions = sorted(potions)
        for i in range(n):
            ##  potions 中寻找 大于等于 success / spells[i]的数目
            ans[i] = m - self.lower_bond(potions, success / spells[i])
        return ans


if __name__ == "__main__":
    a = Solution().successfulPairs([5, 1, 3], [1, 2, 3, 4, 5], 7)
    print(a)
    a = Solution().successfulPairs([3, 1, 2], [8, 5, 8], 16)
    print(a)
