from typing import List
from collections import defaultdict


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        freqmap = defaultdict(int)
        left = 0
        ans = 0
        for right in range(n):
            if nums[right] == 0:
                freqmap[0] += 1
            while freqmap[0] > 1:
                if nums[left] == 0:
                    freqmap[0] -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans - 1

    def longestSubarray2(self, nums: List[int]) -> int:
        n = len(nums)
        freq0 = 0
        left = 0
        ans = 0
        for right in range(n):
            if nums[right] == 0:
                freq0 += 1
            while freq0 > 1:
                if nums[left] == 0:
                    freq0 -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans - 1


if __name__ == "__main__":
    a = Solution().longestSubarray2([0, 1, 1, 1, 0, 1, 1, 0, 1])
    print(a)
