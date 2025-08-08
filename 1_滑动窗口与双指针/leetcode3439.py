from typing import List


class Solution:
    def maxFreeTime(
        self, eventTime: int, k: int, startTime: List[int], endTime: List[int]
    ) -> int:
        ##连续合并k个空闲时间段最优，现在转化为连续合并k个时间段的所得最大空闲时间段的最大值
        ## 新建一数组，存储空闲时间段
        n = len(startTime)
        freeTime = [0] * (n + 1)
        freeTime[0] = startTime[0]
        for i in range(1, n):
            freeTime[i] = startTime[i] - endTime[i - 1]
        freeTime[n] = eventTime - endTime[-1]
        ## 求长度为k的子数组中，最大和
        m = len(freeTime)
        if k + 1 >= m:
            return sum(freeTime)
        windows = 0
        ans = 0
        for i in range(m):
            v = freeTime[i]
            windows += v
            if i < k:
                continue
            ans = max(ans, windows)
            windows -= freeTime[i - k]
        return (ans, freeTime)


if __name__ == "__main__":
    s = Solution().maxFreeTime(5, 2, [0, 1, 2, 3, 4], [1, 2, 3, 4, 5])
    print(s)
    s = Solution().maxFreeTime(10, 1, [0, 2, 9], [1, 4, 10])
    print(s)
    s = Solution().maxFreeTime(10, 1, [0, 2, 4, 5, 9], [1, 4, 5, 6, 10])
    print(s)
