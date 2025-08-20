from typing import List, Tuple


class Solution:
    """
    阅读理解题。
    由于路径可以折返，取连通块中的 distance[i]最小的那条边，即为答案。
    """

    def __init__(self):
        self.ans = float("inf")

    ### 统计 联通块儿中 距离的最小值
    def DFS(
        self, graph: List[List[Tuple[int, int]]], isVisited: List[bool], node: int
    ) -> int:
        if isVisited[node]:
            # 访问过了直接返回最大值，这样不会影响原来的值，因为这里取得是最小值
            return float("inf")
        isVisited[node] = True
        ## 遍历所有与node连接的点
        for j, d in graph[node]:
            self.ans = min(self.ans, d)
            self.DFS(graph, isVisited, j)
        return self.ans

    def minScore(self, n: int, roads: List[List[int]]) -> int:
        ##无向加权图
        ##将其转化为邻接表，用元组来存储
        graph = [[] for _ in range(n + 1)]
        for x, y, z in roads:
            graph[x].append((y, z))
            graph[y].append((x, z))
        isVisited = [False] * (n + 1)
        return self.DFS(graph, isVisited, 1)


if __name__ == "__main__":
    n = 4
    roads = [[1, 2, 9], [2, 3, 6], [2, 4, 5], [1, 4, 7]]
    n = 4
    roads = [[1, 2, 2], [1, 3, 4], [3, 4, 7]]
    n = 14
    roads = [
        [12, 7, 2151],
        [7, 2, 7116],
        [11, 14, 8450],
        [11, 2, 9954],
        [1, 11, 3307],
        [10, 7, 3561],
        [10, 1, 4986],
        [11, 7, 7674],
        [14, 2, 1764],
        [11, 12, 6608],
        [14, 7, 1070],
        [9, 8, 2287],
        [14, 12, 6559],
        [1, 2, 1450],
        [2, 12, 9165],
    ]
    a = Solution()
    s = a.minScore(n, roads)
    print(s)
