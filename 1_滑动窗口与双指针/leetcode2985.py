from typing import List
from collections import defaultdict


class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left = ans = 0
        freqMap = defaultdict(int)
        for right in range(n):
            v = nums[right]
            freqMap[v] += 1
            while freqMap[v] > k:
                freqMap[nums[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans


if __name__ == "__main__":
    a = Solution().maxSubarrayLength([1, 2, 3, 1, 2, 3, 1, 2], 2)
    print(a)
    a = Solution().maxSubarrayLength([5, 5, 5, 5, 5, 5, 5], 4)
    print(a)
