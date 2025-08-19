from typing import List


class Solution:
    def validPath(
        self, n: int, edges: List[List[int]], source: int, destination: int
    ) -> bool:
        ##转换为邻接表的写法
        graph = [[] for _ in range(n)]
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)

        ## 用列表来实现一个双端队列
        queue = [source]
        isVisited = [False] * n
        isVisited[source] = True

        while queue:  ##当列表不为空的时候
            node = queue.pop()
            if node == destination:
                return True
            ## 遍历当前节点的所有连接节点
            for i in graph[node]:
                if not isVisited[i]:
                    isVisited[i] = True
                    queue.append(i)
        return False


if __name__ == "__main__":
    n = 6
    edges = [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]]
    graph = [[] for _ in range(n)]
    for x, y in edges:
        graph[x].append(y)
        graph[y].append(x)
    print(graph)
