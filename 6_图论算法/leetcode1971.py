from typing import List


class Solution:
    def __init__(self) -> None:
        self.result = []
        self.path = []
        
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:      
        #从source开始，深度优先遍历，判断是否能够到达destination
        # 可以将edges转化为邻接矩阵
        mat = [[0] * n for _ in range(n)]
        for s in edges:
            mat[s[0]][s[1]] = 1
        self.path.append(source)
        self.bfs(mat,source,destination)
        ###得到result
        for s in self.result:
            if s[-1] == destination:
                return True
        return False
    def bfs(self, mat: List[List[int]], x: int, destination: int):
        if x == destination:
            self.result.append(self.path.copy())
            return
        for j in range(len(mat)):
            if mat[x][j] == 1:
                self.path.append(j)
                self.bfs(mat,j,destination)
                del self.path[len(self.path) - 1]
            
            



class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        result = []
        path = []
        n = len(graph)
        path.append(0)
        def dfs(x: int, graph: List[List[str]]):
            if path[-1] == n - 1:
                result.append(path.copy())
                return
            ## 如果没有到达n个长度，那么应该遍历x连接的所有节点
            for cur in graph[x]:
                path.append(cur)
                dfs(cur,graph)
                del path[len(path) - 1]
        dfs(0,graph)
        return result


            

if __name__=='__main__':
    edges = [[0,1],[0,2],[3,5],[5,4],[4,3]]
    n = 6
    a=Solution()
    a.validPath(n,edges,0,5 )
    # mat = [[0 for _ in range(n)] for _ in range(n)]
    # for s in edges:
    #     mat[s[0]][s[1]] = 1
    # print(mat)