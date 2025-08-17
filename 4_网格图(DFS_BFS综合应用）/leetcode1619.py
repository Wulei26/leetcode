from typing import List
class Solution:
    def dfs(self, land: List[List[int]], i: int, j: int ) -> int:
        ## 返回land中坐标为i j 的池塘的面积大小
        if i < 0 or i >= len(land) or j < 0 or j >= len(land[0]): ## 不在池塘范围内
            return 0
        if land[i][j] != 0 or land[i][j] == -1: # 陆地或者已经计算过了
            return 0
        land[i][j] = -1
        return (1 + 
                self.dfs(land, i -1, j) + self.dfs(land,i + 1, j)+self.dfs(land, i, j - 1) + self.dfs(land, i, j + 1)+
                self.dfs(land, i -1, j - 1) + self.dfs(land, i - 1, j -1) + self.dfs(land,i+1, j -1 ) + self.dfs(land,i+1,j +1))
    

    def pondSizes(self, land: List[List[int]]) -> List[int]:
        n = len(land)
        m = len(land[0])
        ans = []
        for i in range(n):
            for j in range(m):
                if land[i][j] == 0:
                    area = self.dfs(land, i,j)
                    ans.append(area)
        return sorted(ans)
        