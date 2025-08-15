from typing import List


class Solution:
    def dfs(self, grid: List[List[int]], i: int, j: int) -> int:
        if (
            i < 0
            or i >= len(grid)
            or j < 0
            or j >= len(grid[0])
            or grid[i][j] == 0
            or grid[i][j] == -1
        ):
            return 0
        area = grid[i][j]
        grid[i][j] = -1
        return (
            area
            + self.dfs(grid, i - 1, j)
            + self.dfs(grid, i + 1, j)
            + self.dfs(grid, i, j - 1)
            + self.dfs(grid, i, j + 1)
        )

    def countIslands(self, grid: List[List[int]], k: int) -> int:
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] > 0:
                    landArea = self.dfs(grid, i, j)
                    if landArea % k == 0:
                        ans += 1
        return ans


if __name__ == "__main__":
    a = Solution().countIslands(
        [
            [0, 2, 1, 0, 0],
            [0, 5, 0, 0, 5],
            [0, 0, 1, 0, 0],
            [0, 1, 4, 7, 0],
            [0, 2, 0, 0, 8],
        ],
        5,
    )
    print(a)
