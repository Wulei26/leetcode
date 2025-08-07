from collections import defaultdict


class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        n = len(s)
        freqmap = defaultdict(int)
        left = 0
        ans = 0
        for right in range(n):
            v = s[right]
            freqmap[v] += 1
            while freqmap[v] > 2:
                freqmap[s[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans


if __name__ == "__main__":
    a = Solution().maximumLengthSubstring("bcbbbcba")
    print(a)
