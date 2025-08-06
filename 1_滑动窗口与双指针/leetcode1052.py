from typing import List


class Solution:
    def maxSatisfied(
        self, customers: List[int], grumpy: List[int], minutes: int
    ) -> int:
        """
        1. 不生气时的顾客是一定可以拿到的，这是最基本的,也就是每天的顾客的最小值
        2. 剩下就是在长度为minutes的时间中, 可以争取到的客户，如何争取到最多？==》在长度为minutes的区间中，grump为1 对应的customers的最大值
        """
        n = len(customers)
        ans = base = 0
        windows = 0  # 记录长度为minutes的时间中，生气的顾客数目
        for i in range(n):
            if grumpy[i] == 0:
                base += customers[i]  ## base 数目
            else:
                windows += customers[i]
            if i < minutes - 1:
                continue
            # 离开窗口
            ans = max(ans, windows)
            if grumpy[i - minutes + 1] == 1:
                windows -= customers[i - minutes + 1]
        return ans + base


if __name__ == "__main__":
    a = Solution().maxSatisfied([1, 0, 1, 2, 1, 1, 7, 5], [0, 1, 0, 1, 0, 1, 0, 1], 3)
    print(a)
    a = Solution().maxSatisfied([1], [0], 1)
    print(a)
