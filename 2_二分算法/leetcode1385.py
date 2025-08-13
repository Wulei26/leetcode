from typing import List
from bisect import bisect_left


class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        ## 绝对值展开对于 元素arr1[i] 不存在任何元素 j 满足 arr1[i] -d <= arr2[j] <= arr1[i] + d
        ##
        n, m = len(arr1), len(arr2)
        ans = 0
        arr2.sort()
        for x in arr1:
            i = bisect_left(arr2, x - d)
            if i == len(arr2) or arr2[i] > x + d:
                ans += 1
        return ans


if __name__ == "__main__":
    a = Solution().findTheDistanceValue([4, 5, 8], [10, 9, 1, 8], 2)
    print(a)
