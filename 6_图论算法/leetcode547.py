from typing import List


class Solution:
    def dfs(self, isConnected: List[List[int]], isVisited: List[bool], i: int):
        isVisited[i] = True
        ## 继续对节点i相邻的点进行访问
        for j in range(len(isConnected)):
            if isConnected[i][j] == 1 and isVisited[j] == False:
                self.dfs(isConnected, isVisited, j)

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        ## 使用一个数组记录是否被遍历过
        isVisited = [False] * 201
        n = len(isConnected)
        ans = 0
        for i in range(n):
            if not isVisited[i]:  ## 没有被访问
                ans += 1
                self.dfs(isConnected, isVisited, i)
        return ans
