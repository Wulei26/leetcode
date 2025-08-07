class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n = len(s)
        left = 0
        ans = 0
        cost = 0
        for right in range(n):
            cost += abs(ord(s[right]) - ord(t[right]))
            while cost > maxCost:
                cost -= abs(ord(s[left]) - ord(t[left]))
                left += 1
            ans = max(ans, right - left + 1)
        return ans


if __name__ == "__main__":
    a = Solution().equalSubstring("abcd", "bcdf", 3)
    print(a)
    a = Solution().equalSubstring("abcd", "acde", 0)
    print(a)
