from typing import List
import heapq


class Solution:
    def maxProbability(
        self,
        n: int,
        edges: List[List[int]],
        succProb: List[float],
        start_node: int,
        end_node: int,
    ) -> float:
        graph = [[] for _ in range(n)]
        for i, edge in enumerate(edges):
            graph[edge[0]].append((edge[1], succProb[i]))
            graph[edge[1]].append((edge[0], succProb[i]))

        visited = [False] * n
        MAX = float("inf")

        dis = [0] * n
        dis[start_node] = 1

        heap = []
        heapq.heappush(heap, (-1, start_node))

        while heap:
            cur_dis, cur_node = heapq.heappop(heap)
            cur_dis = -cur_dis
            if visited[end_node]:
                return dis[end_node]
            if visited[cur_node]:
                continue
            visited[cur_node] = True

            for edge in graph[cur_node]:
                ##是否能到达edge
                tmp = edge[1] * cur_dis
                if not visited[edge[0]] and dis[edge[0]] < tmp:
                    dis[edge[0]] = tmp
                    heapq.heappush(heap, (-tmp, edge[0]))
        return dis[end_node]


if __name__ == "__main__":
    n = 3
    edges = [[0, 1], [1, 2], [0, 2]]
    succProb = [0.5, 0.5, 0.2]
    start = 0
    end = 2
    a = Solution().maxProbability(n, edges, succProb, start, end)
    print(a)
