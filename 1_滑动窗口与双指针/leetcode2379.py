class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        ans = float("inf")
        windows = 0  # 当前窗口有几个白色块
        for i in range(n):
            s = blocks[i]
            if s == "W":
                windows += 1
            if i < k - 1:
                continue
            ans = min(ans, windows)
            ## 离开窗口
            if blocks[i - k + 1] == "W":
                windows -= 1
        return ans


if __name__ == "__main__":
    a = Solution().minimumRecolors("WBBWWBBWBW", 7)
    print(a)
    a = Solution().minimumRecolors("WBWBBBW", 3)
    print(a)
