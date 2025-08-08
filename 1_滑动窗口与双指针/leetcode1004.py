from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        left = 0
        count_zero = 0
        for right in range(n):
            v = nums[right]
            if v == 0:
                count_zero += 1
            while count_zero > k:
                if nums[left] == 0:
                    count_zero -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans


if __name__ == "__main__":
    a = Solution().longestOnes([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2)
    print(a)
    a = Solution().longestOnes(
        [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3
    )
    print(a)
