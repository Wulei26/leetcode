from typing import List
import heapq

class Solution:
    def minTime(self, n: int, edges: List[List[int]]) -> int:
        MAX = float('inf')
        graph = [[] for _ in range(n)]
        for a,b,c,d in edges:
            graph[a].append((b,c,d))
        visited = [False] * n
        dis = [MAX] * n
        dis[0] = 0

        heap = []

        heapq.heappush(heap,(0,0))

        while heap:

            cur_dis, cur_node = heapq.heappop(heap)

            if visited[cur_node]:
                continue
            visited[cur_node] = True

            for edge in graph[cur_node]:
                nt = cur_dis
                ###判断
                ###是否需要等待
                if cur_dis < edge[1]: ##这种情况就需要等待
                    ##等待的时间 edge[1] - cur_dis
                    ## 总的时间 cur_dis + edge[1] - cur_dis + 1
                    nt = edge[1] + 1
                elif cur_dis > edge[2]: #时间已经过了
                    continue
                else:##在范围内
                    nt = cur_dis + 1
                ###如果找到了 更优路径
                if nt < dis[edge[0]]:
                    dis[edge[0]] = nt
                    heapq.heappush(heap,(nt,edge[0]))
        return dis[n-1] if dis[n-1] != MAX else -1
                
if __name__=='__main__':
    n = 4
    edges = [[0,1,0,3],[1,3,7,8],[0,2,1,5],[2,3,4,7]]
    # n = 3
    # edges = [[0,1,0,1],[1,2,2,5]]
    # edges = [[0,2,5,7],[2,1,4,9]]
    a = Solution().minTime(n,edges)
    print(a)






        