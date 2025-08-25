from typing import List
import heapq

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        ###表示从上下左右四个方向移动
        dirs = [(-1,0),(1,0),(0,1),(0,-1)]
        ## t,x,y表示从原点道道x,y的最短时间
        heap = []
        heapq.heappush(heap,(0,0,0))
        n, m = len(moveTime),len(moveTime[0])
        MAX = float('inf')
        times = [[MAX] * m for _ in range(n)] ## time表示各个点到达原点的最短时间
        times[0][0] = 0

        while heap:
            t,x,y = heapq.heappop(heap)
            ### 这里其实可以优化一下，如果t >times[x][y]的话，说明到过这里，有比这个更优的路径，因此不需要再判断了
            if t > times[x][y]:
                continue
            ###遍历x，y的上下左右
            for dx, dy in dirs:
                nx,ny = x + dx, y + dy
                ## 保证其在数组范围内
                if 0<= nx < n and 0 <= ny < m:
                    ## 是否需要等待
                    if t < moveTime[nx][ny]: ##为什么需要这个判断，这里需要读懂题意，movetime[i][j]表示每个格子的时间限制
                           ##也就是说，x必须达到movetime[i][j]的时间，才能进入这个格子，否则就不能进入这个格子
                        ####因此，如果没有达到moveTime[nx][ny]要求的时间，则需要等待(moveTime[nx][ny] - t)的时间，那么总到达时间为：t + (moveTime[nx][ny] - t) + 1 = moveTime[nx][ny] + 1。
                        nt = moveTime[nx][ny] + 1
                    else:
                        nt = t + 1
                    ###是否筛选到了更优路径
                    if nt < times[nx][ny]:
                        times[nx][ny] = nt
                        heapq.heappush(heap,(nt,nx,ny))
        return times[n-1][m-1]
                        


