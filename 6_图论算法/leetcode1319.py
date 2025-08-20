from typing import List


class Solution:
    ###计算连通块的数量
    def DFS(self, graph: List[List[int]], isVisited: List[bool], node: int) -> int:
        if isVisited[node]:
            return 0
        isVisited[node] = True
        size = 1
        for nextNode in graph[node]:
            if not isVisited[nextNode]:
                size += self.DFS(graph, isVisited, nextNode)
        return size

    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        ## n个计算机至少需要n -1 根线
        if len(connections) < n - 1:
            return -1
        ##将其转化为邻接表
        graph = [[] for _ in range(n)]
        for x, y in connections:
            graph[x].append(y)
            graph[y].append(x)
        isVisited = [False] * n
        ##统计连通块的数量和大小
        res = []
        for i in range(n):
            if not isVisited[i]:
                size = self.DFS(graph, isVisited, i)
                res.append(size)
        ###统计可以用来连接别的连通块的线，n个节点至少需要n-1条线就可以连接起来，其余的都是多的，可以拆开
        redundancy = sum(res) - len(res)
        ##也就是说我需要redundancy 这个数量的线就可以将连通块的内部连接起来
        ##那么连接m个连通块至少需要m-1根线
        ##也就是说我实际的线的数量 减去redundancy 能否覆盖掉 m-1,如果可以，那就能连起来，否则就不行
        if len(connections) - redundancy < len(res) - 1:
            return -1
        ##可以覆盖掉，那么只需要将不同的连通块连接起来就好了
        return len(res) - 1


if __name__ == "__main__":
    n = 6
    connections = [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3]]
    a = Solution()
    print(a.makeConnected(n, connections))
