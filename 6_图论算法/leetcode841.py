from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        ## rooms相当于有向图，从0号开始递归遍历，看能否遍历到所有节点，如果遍历结束有未被访问的节点，则为False
        n = len(rooms)
        isVisited = [False] * n
        self.dfs(rooms, isVisited, 0)
        ## 如果还有False，那么就返回False
        for ans in isVisited:
            if not ans:
                return False
        return True

    def dfs(self, rooms: List[List[int]], isVisited: List[bool], node: int):
        if isVisited[node]:
            return
        isVisited[node] = True
        for LinkNode in rooms[node]:
            self.dfs(rooms, isVisited, LinkNode)


if __name__ == "__main__":
    rooms = [[1, 3], [3, 0, 1], [2], [0]]
    rooms = [[1], [2], [3], []]
    a = Solution().canVisitAllRooms(rooms)
    print(a)
