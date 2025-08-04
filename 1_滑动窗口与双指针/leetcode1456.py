from typing import List


class Solution:
    """
    定长窗口
    1 <= s.length <= 10^5
    s 由小写英文字母组成
    1 <= k <= s.length
    """

    def maxVowels(self, s: str, k: int) -> int:
        ans = tmp = 0
        n = len(s)
        for i in range(n):
            cur = s[i]
            if cur in "aeiou":
                tmp += 1
            if i < k - 1:
                continue
            ans = max(tmp, ans)
            # 离开窗口
            if s[i - k + 1] in "aeiou":
                tmp -= 1
        return ans


if __name__ == "__main__":
    A = Solution()
    ans = A.maxVowels(s="aeiou", k=3)
    print(ans)
    ans = A.maxVowels(s="abciiidef", k=3)
    print(ans)
