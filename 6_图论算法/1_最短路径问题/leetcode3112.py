from typing import List
import heapq


class Solution:
    def minimumTime(self, n: int, edges: List[List[int]], disappear: List[int]) -> List[int]:
        ###邻接表存储
        graph = [[] for _ in range(n)]
        for x,y,z in edges:
            graph[x].append((y,z))
            graph[y].append((x,z))
        
        MAX = float('inf')

        ans = [MAX]* n
        ans[0] = 0

        visited = [False] * n

        heap = []

        heapq.heappush(heap,(0,0)) ## 表示到达原点的最短距离,前面表示时间，后面表示节点

        while heap:
            cur_time, cur_node = heapq.heappop(heap)
            if visited[cur_node]:
                continue
            visited[cur_node] = True

            ## 遍历所有节点

            for edge in graph[cur_node]:
                tmp = cur_time + edge[1]
                ##如果
                if not visited[edge[0]] and  tmp < ans[edge[0]] and tmp < disappear[edge[0]]:
                    ##说明是能到达的
                    ans[edge[0]] = tmp
                    heapq.heappush(heap,(tmp,edge[0]))
        return list(map(lambda x : -1 if x == MAX else x , ans))
    
if __name__=='__main__':
    n = 3
    edges = [[0,1,2],[1,2,1],[0,2,4]]
    disappear = [1,1,5]
    # n = 3
    # edges = [[0,1,2],[1,2,1],[0,2,4]]
    # disappear = [1,3,5]
    n = 2
    edges = [[0,1,1]]
    disappear = [1,1]
    a = Solution().minimumTime(n,edges,disappear)
    print(a)




