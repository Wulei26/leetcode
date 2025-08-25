from typing import List
import heapq


class Graph:
    def __init__(self, n: int, edges: List[List[int]]):
        self.g = [[float('inf')] * n for _ in range(n)]  # 邻接矩阵
        for x, y, w in edges:
            self.g[x][y] = w  # 添加一条边（题目保证没有重边）

    def addEdge(self, e: List[int]) -> None:
        self.g[e[0]][e[1]] = e[2]  # 添加一条边（题目保证这条边之前不存在）

    def shortestPath(self, start: int, end: int) -> int:
        n = len(self.g)
        dis = [float('inf')] * n  # 从 start 出发，到各个点的最短路，如果不存在则为无穷大
        dis[start] = 0
        vis = [False] * n
        while True:  # 至多循环 n 次
            x = -1
            for i, (b, d) in enumerate(zip(vis, dis)):
                if not b and (x < 0 or d < dis[x]):
                    x = i
            if x < 0 or dis[x] == float('inf'):  # 所有从 start 能到达的点都被更新了
                return -1  # 无法到达终点
            if x == end:  # 找到终点，提前退出
                return dis[x]
            vis[x] = True  # 标记，在后续的循环中无需反复更新 x 到其余点的最短路长度
            for y, w in enumerate(self.g[x]):
                if dis[x] + w < dis[y]:
                    dis[y] = dis[x] + w  # 更新最短路长度