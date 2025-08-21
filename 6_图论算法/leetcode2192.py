from typing import List
from collections import deque


class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        ##既然是找祖先，那么将所有的单向边反过来，那么原来的起始点就变成了终点
        graph = [[] for _ in range(n)]
        for x, y in edges:
            graph[y].append(x)
        ##这构成了一个逆向的邻接表
        ## 那么从i出发，能够到达的所有点就是i的答案
        ans = [[] for _ in range(n)]

        ## 使用广度优先遍历

        for i in range(n):
            tmp = []
            isVisited = [False] * n
            isVisited[i] = True
            q = deque([i])  ##从i出发
            while q:
                x = q.popleft()
                for y in graph[x]:
                    if not isVisited[y]:
                        isVisited[y] = True
                        q.append(y)
                        tmp.append(y)
            ans[i] = sorted(tmp)
        return ans


if __name__ == "__main__":
    n = 8
    edgeList = [[0, 3], [0, 4], [1, 3], [2, 4], [2, 7], [3, 5], [3, 6], [3, 7], [4, 6]]
    a = Solution().getAncestors(n, edgeList)
    print(a)
