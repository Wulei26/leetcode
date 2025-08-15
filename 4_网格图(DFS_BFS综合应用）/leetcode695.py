from typing import List


class Solution:
    def dfs(self, grid: List[List[int]], i: int, j: int) -> int:
        if (
            i < 0
            or i >= len(grid)
            or j < 0
            or j >= len(grid[0])
            or grid[i][j] == 0
            or grid[i][j] == 2
        ):
            return 0
        grid[i][j] = 2
        return (
            1
            + self.dfs(grid, i - 1, j)
            + self.dfs(grid, i + 1, j)
            + self.dfs(grid, i, j - 1)
            + self.dfs(grid, i, j + 1)
        )

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    area = self.dfs(grid, i, j)
                    ans = max(ans, area)
        return ans


if __name__ == "__main__":
    a = Solution().maxAreaOfIsland(
        grid=[
            [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
        ]
    )
    print(a)
