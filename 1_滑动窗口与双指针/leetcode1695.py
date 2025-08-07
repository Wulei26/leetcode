from typing import List
from collections import defaultdict


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        left = ans = 0
        windowsSum = 0
        freqMap = defaultdict(int)
        for right in range(n):
            v = nums[right]
            ##加入到freqMap中
            freqMap[v] += 1
            windowsSum += v
            while freqMap[v] > 1:
                freqMap[nums[left]] -= 1  ##移除窗口，记得windows也要更新
                windowsSum -= nums[left]
                left += 1
            ans = max(ans, windowsSum)
        return ans


if __name__ == "__main__":
    A = Solution().maximumUniqueSubarray([4, 2, 4, 5, 6])
    print(A)
    A = Solution().maximumUniqueSubarray([5, 2, 1, 2, 5, 2, 1, 2, 5])
    print(A)
