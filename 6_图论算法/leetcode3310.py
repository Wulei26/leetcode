from typing import List


class Solution:
    def DFS(self, graph: List[List[int]], isVisited: List[int], node: int) -> None:
        if isVisited[node]:
            return
        isVisited[node] = True
        for nextNode in graph[node]:
            if not isVisited[nextNode]:
                self.DFS(graph, isVisited, nextNode)

    def remainingMethods(
        self, n: int, k: int, invocations: List[List[int]]
    ) -> List[int]:
        ##有向无权图
        ##根据题意可以知道，处于k这个联通块之外的 节点即为答案
        graph = [[] for _ in range(n)]
        for x, y in invocations:
            graph[x].append(y)  ##有向图
        isVisited = [False] * n
        ans = []
        self.DFS(graph, isVisited, k)
        """
        你需要删除所有可能有 bug 的方法。
        如果删除后无法编译（剩余的方法调用了可疑的方法），那么返回数组 [0,1,2,⋯,n−1]。
        """
        for i in range(n):
            if not isVisited[i]:
                ans.append(i)
        ## ans是删除了可疑方法的剩余方法。看看是否有节点调用了可疑方法，如果有，那么直接返回原数组
        for x, y in invocations:
            ## 如果x是剩余方法，但是y是可疑方法，那么就返回
            if not isVisited[x] and isVisited[y]:
                return [i for i in range(n)]
        return ans


if __name__ == "__main__":
    n = 3
    k = 2
    invocations = [[1, 2], [0, 1], [2, 0]]
    n = 5
    k = 0
    invocations = [[1, 2], [0, 2], [0, 1], [3, 4]]
    invocations = [[1, 2], [0, 1], [3, 2]]
    invocations = [[1, 2], [0, 2], [0, 1], [3, 4]]
    a = Solution()
    print(a.remainingMethods(5, 0, invocations))
