from typing import List, Tuple
import math


class Solution:
    def __init__(self) -> None:
        self.path = []
    def DFS(
        self, graph: List[List[int]], isVisited: List[bool], node: int) -> None:
        if isVisited[node]:
            return
        isVisited[node] = True
        self.path.append(node)
        for nextNode in graph[node]:
            if not isVisited[nextNode]:
                self.DFS(graph, isVisited, nextNode)
        return

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
                self.DFS(graph, isVisited, i, )
                blocks.append(self.path.copy())
                self.path.clear()
        ###计算每个连通分量存在的边的个数
        sideCount = [0] * len(blocks)
        for b in range(len(blocks)):
            tmp = 0
            for i in blocks[b]:
                tmp += len(graph[i])
            sideCount[b] = tmp // 2
        ### 如果是完全完全联通分量，那么对应的连通块的边的数量应该是C(n,2) n是这个连通块的节点数量
        ans = 0
        for i in range(len(blocks)):
            if sideCount[i] == 0:
                ans += 1
                continue
            if math.comb(len(blocks[i]),2) == sideCount[i]:
                ans += 1
        return ans

#### 可以换一种空间复杂度更低的方法
class Solution2:
    ##只统计连通块点的数量和边的数量
    def __init__(self) -> None:
        self.count = 0
        self.sides = 0
    def DFS(self, graph: List[List[int]], isVisited: List[bool], node: int) -> None:
        if isVisited[node]:
            return
        isVisited[node] = True
        self.count += 1
        self.sides += len(graph[node])
        for nextNode in graph[node]:
            if not isVisited[nextNode]:
                self.DFS(graph, isVisited, nextNode)

    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        ##首先它一定是一个连通块
        ##统计每个联通块的节点数量
        graph = [[] for _ in range(n)]
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        isVisited = [False] * n
        blocks:List[Tuple[int, int]] = []
        ans = 0
        for i in range(n):
            if not isVisited[i]:
                self.DFS(graph, isVisited, i)
                blocks.append((self.count, self.sides // 2))
                #联通分量节点的个数后面是联通分量的边数
                if self.sides // 2 == math.comb(self.count, 2) or self.count == 1:
                    ans += 1
                self.count = 0
                self.sides = 0
        return ans


if __name__ == "__main__":
    n = 6
    edges = [[0, 1], [0, 2], [1, 2], [3, 4]]
    n = 6
    edges = [[0, 1], [0, 2], [1, 2], [3, 4], [3, 5]]
    a = Solution2()
    print(a.countCompleteComponents(n, edges))
