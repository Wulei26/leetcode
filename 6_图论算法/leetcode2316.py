from typing import List


class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        ##统计联通块的大小和数量
        ## edges转化为邻接表
        graph = [[] for _ in range(n)]
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)

        isVisited = [False] * n
        ans = total = 0
        for i in range(n):
            if not isVisited[i]:  ##还没被访问的，那就是一个联通块儿
                size = self.DFS(graph, isVisited, i)
                ans += size * total
                total += size
        return ans

    ## 统计 node 连接的节点的数量
    def DFS(self, graph: List[List[int]], isVisited: List[bool], node: int) -> int:
        if isVisited[node]:
            return 0
        isVisited[node] = True
        size = 1
        for nextNode in graph[node]:
            if not isVisited[nextNode]:
                size += self.DFS(graph, isVisited, nextNode)
        return size
