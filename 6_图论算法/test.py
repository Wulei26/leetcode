from collections import deque
from typing import List


class Solution:
    def validPath(
        self, n: int, edges: List[List[int]], source: int, destination: int
    ) -> bool:
        mat = [[0] * n for _ in range(n)]
        for u, v in edges:
            mat[u][v] = mat[v][u] = 1

        visited = [False] * n
        stack = [source]
        visited[source] = True

        while stack:
            node = stack.pop()
            if node == destination:
                return True
            for neighbor in range(n):
                if mat[node][neighbor] and not visited[neighbor]:
                    visited[neighbor] = True
                    stack.append(neighbor)

        return False


if __name__ == "__main__":
    sol = Solution()
    n = 6
    edges = [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]]
    print(sol.validPath(n, edges, 0, 5))  # 输出: False（0和5不在同一连通分量）
    print(sol.validPath(n, edges, 3, 5))  # 输出: True（3→5直接可达）
