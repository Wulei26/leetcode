from collections import defaultdict


class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        n = len(maxLetters)
        subFreq = defaultdict(int)
        left = 0
        windowsFreq = defaultdict(int)  ## 记录窗口中字符的频数

        for right in range(n):
            v = s[right]
            windowsFreq[v] += 1
            if right < minSize - 1:
                continue
            ##什么时候满足要求
            if (
                len(windowsFreq) <= maxLetters
                and (right - left + 1) >= minSize
                and (right - left + 1) <= maxLetters
            ):
                subFreq[s[left : right + 1]] += 1
            # 离开窗口
            windowsFreq[s[left]] -= 1
            if windowsFreq[s[left]] == 0:
                del windowsFreq[s[left]]


if __name__ == "__main__":
    a = Solution().maxFreq("aababcaab", 2, 3, 4)
