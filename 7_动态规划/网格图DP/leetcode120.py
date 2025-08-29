from typing import List
from functools import cache


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        ##新建一个一摸一样的数组
        dp = [[0] * i for i in range(1, n + 1)]
        ##首先左边这条斜边一定是可以计算出的，因为只有一种移动方式
        count = 0
        for i in range(n):
            count += triangle[i][0]
            dp[i][0] = count
        ###右边这条边也是
        count = 0
        for i in range(n):
            count += triangle[i][-1]
            dp[i][-1] = count

        ##对于中间的
        for i in range(1, n):
            layer = triangle[i]
            length = len(layer)
            for j in range(1, length - 1):
                dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1]) + triangle[i][j]
        return min(dp[n - 1])


class Solution2:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        ##拆解成一个子问题
        # 定义dfs（i，j)为从i，j出发移动到最后一排的元素路径的最小值
        ## 那么i,j你能走到哪里？
        ##  1.走到i+1,j 那么子问题变成了 dfs(i+1,j)
        ##  2.走到i+1,j+1,那么子问题就变成dfs(i+1,j+1)
        ##直到走到了最后一层，也就是dfs（i，j)中的i为n-1,那么就返回当前triangel的值就好了
        n = len(triangle)

        @cache
        def dfs(i: int, j: int) -> int:
            if i == n - 1:
                return triangle[i][j]
            return min(dfs(i + 1, j), dfs(i + 1, j + 1)) + triangle[i][j]

        return dfs(0, 0)


if __name__ == "__main__":
    triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
    a = Solution2().minimumTotal(triangle)
    print(a)
