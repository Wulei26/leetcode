from typing import List
from collections import deque


class Solution:

    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        MAX = float("inf")
        ##计算节点k到所有节点的最短路径
        ##将times转化为邻接矩阵
        mat = [[MAX] * (n + 1) for _ in range(n + 1)]
        for x, y, z in times:
            mat[x][y] = z
        # dis存储节点k到每个节点的最短距离
        dis = [float("inf")] * (n + 1)
        ## visited 记录节点是否被访问过
        visited = [False] * (n + 1)
        dis[k] = 0
        ### 计算k到其余所有节点的最短路径
        for _ in range(n):
            min_value = MAX
            min_value_index = MAX
            for index in range(1, n + 1):  ##找出当前没有访问过的点到达源点的最小值
                if (
                    not visited[index] and dis[index] < min_value
                ):  ## 后面这个表达式，只有当 dis[index]有值的时候才会是True
                    min_value = dis[index]
                    min_value_index = index
                ###现在就找到了当前节点连接的所有节点 距离源点距离最小的那个点；
                ## 如果是第一次执行这个循环，min_value 一定是 0 ，min_value_index一定是k
            if min_value == MAX:
                break  ###说明当前节点没有连接到别的节点了

            visited[min_value_index] = True

            ## 更新dis，如果一个节点y，y到源点的距离可以有两种
            ## 1、y经过某个点到达源点 start -> x ->y : dir[x] + graph[x][y]
            ## 2、 y直接和源点的距离 star -> y       : dir[x]
            for index in range(1, n + 1):
                dis[index] = min(
                    dis[index], dis[min_value_index] + mat[min_value_index][index]
                )

        ###如果能够到达所有节点，那么返回dis的最大值，如果最大值是 MAX，那么返回-1
        ans = -MAX
        for i in range(1, n + 1):
            ans = max(ans, dis[i])
        if ans == MAX:
            return -1
        return ans


if __name__ == "__main__":
    a = Solution()
    a.networkDelayTime([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2)
    print(a)
