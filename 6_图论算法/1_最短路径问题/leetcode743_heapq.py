from typing import List
import heapq


class Solution:

    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        MAX = float("inf")
        ## 转换成邻接表
        graph = [[] for _ in range(n + 1)]
        for x, y, z in times:
            graph[x].append((y, z))  ## 有向图

        dis = [MAX] * (n + 1)
        visited = [False] * (n + 1)

        dis[k] = 0
        pq = []
        heapq.heappush(pq, (0, k))
        ### 这个元组存储的当前节点，和当前节点距离源点的最小值

        while pq:
            cur_dist, cur_node = heapq.heappop(pq)  ## 如果是进入循环就抛出 源节点
            ## 这里返回的就是 距离源点最近且没被访问过的节点

            if visited[cur_node]:
                continue

            visited[cur_node] = True

            for edge in graph[cur_node]:  ##访问当前节点 所连接的所有点中，距离最小的点
                if (
                    not visited[edge[0]] and cur_dist + edge[1] < dis[edge[0]]
                ):  ###什么时候更新值
                    ## cur_dist + edge[1] 就是cur_node 连接的节点到源点的距离 start -> x ->y
                    ### dis[edge[0]] 就是 这个点不经过cur_node 直接连接到源点
                    dis[edge[0]] = cur_dist + edge[1]
                    heapq.heappush(
                        pq, (dis[edge[0]], edge[0])
                    )  ## 这里加入的节点会进行排序，排到堆顶的一定是dis[edge[0]]最小的点, 也就是当前节点所连接的所有点中距离源点最近的点

        ans = -MAX
        for i in range(1, n + 1):
            ans = max(ans, dis[i])
        if ans == MAX:
            return -1
        return ans


if __name__ == "__main__":
    times = [
        [1, 2, 1],
        [1, 3, 4],
        [2, 3, 2],
        [2, 4, 5],
        [3, 4, 2],
        [4, 5, 3],
        [2, 6, 4],
        [5, 7, 4],
        [6, 7, 9],
    ]
    n = 7
    k = 1
    a = Solution().networkDelayTime(times, n, k)
