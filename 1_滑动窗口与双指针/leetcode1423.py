from typing import List


class Solution:
    """
    把这个列表想象成一个环形列表
        1 <= cardPoints.length <= 10^5
        1 <= cardPoints[i] <= 10^4
        1 <= k <= cardPoints.lengt
    """

    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        if k >= n:
            return sum(cardPoints)
        ans = windows = 0
        # 从列表的第n-k个元素开始，与列表的第1-k个元素组成一个列表，寻找最大的子数组和
        newCard = cardPoints[n - k : n] + cardPoints[0:k]
        for i in range(k * 2):
            s = newCard[i]
            windows += s
            if i < k - 1:
                continue
            ans = max(ans, windows)
            # 离开
            windows -= newCard[i - k + 1]
        return ans


if __name__ == "__main__":
    a = Solution().maxScore([1, 2, 3, 4, 5, 6, 1], 3)
    print(a)
    a = Solution().maxScore([2, 2, 2], 2)
    print(a)
    a = Solution().maxScore([1, 79, 80, 1, 1, 1, 200, 1], 3)
    print(a)
