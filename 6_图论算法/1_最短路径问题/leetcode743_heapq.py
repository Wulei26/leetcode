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
                    ### 为什么这里不需要min（cur_dist + edge[1]， dis[edge[0]]）了
                    ### 因为dis[edge[0]]初始化是MAX，而cur + edge[1] 一定是一个数，所以如果这个节点未被访问过，那么就一定会被更新
                    ## 所以这里是将cur_node连接的所有点进行加入，而且利用堆排序，最上面的就是距离最近的点
                    ## 为什么这里不需要显式的比较 min(start -> x ->y,start->y)。就拿 1，2， 3举例子，1->2->3 的距离小于1->3的距离
                    ## 在初始的时候，也就是cur_node为start的时候，就会更新dis[3]的距离为4，然后我们再做判断 cur_dist + edge[1] < dis[edge[0]] 如果这个
                    ## 条件为真，那么就说明找到了比直接与源点相连 更短的路径，这个时候我们再更新dis[3]，这就是为什么我们不需要再用min比较了
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
