from typing import List


class Solution:
    def DFS(
        self, graph: List[List[int]], isVisited: List[bool], node: int, path: List[int]
    ) -> List[int]:
        if isVisited[node]:
            return []
        isVisited[node] = True
        path.append(node)
        for nextNode in graph[node]:
            if not isVisited[nextNode]:
                path = path + self.DFS(graph, isVisited, nextNode, path)
        return path

    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        ##首先它一定是一个连通块
        ##统计每个联通块的节点数量
        graph = [[] for _ in range(n)]
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        isVisited = [False] * n
        blocks = []
        for i in range(n):
            if not isVisited[i]:
                blocks.append(self.DFS(graph, isVisited, i, []))
        return blocks


if __name__ == "__main__":
    n = 6
    edges = [[0, 1], [0, 2], [1, 2], [3, 4]]
    a = Solution()
    print(a.countCompleteComponents(n, edges))
