from typing import List


class Solution:
    """
    1 <= arr.length <= 105
    1 <= arr[i] <= 104
    1 <= k <= arr.length
    0 <= threshold <= 104"""

    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        n = len(arr)
        ans = 0
        tmp = 0
        for i in range(n):
            v = arr[i]
            tmp += v
            if i < k - 1:
                continue
            if tmp >= threshold * k:
                ans += 1
            # 移除元素
            tmp -= arr[i - k + 1]
        return ans


if __name__ == "__main__":
    a = Solution().numOfSubarrays([2, 2, 2, 2, 5, 5, 5, 8], 3, 4)
    print(a)
    a = Solution().numOfSubarrays([11, 13, 17, 23, 29, 31, 7, 5, 2, 3], 3, 5)
    print(a)
