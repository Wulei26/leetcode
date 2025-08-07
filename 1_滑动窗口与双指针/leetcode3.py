from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 定义一个map，key为字符，value为字符出现的频次
        charmap = defaultdict(int)
        n = len(s)
        left = 0
        ans = 0
        for right in range(n):
            # 将字符加入map
            v = s[right]
            charmap[v] += 1
            while charmap[v] > 1:
                charmap[s[left]] -= 1
                left += 1
            ans = max(right - left + 1, ans)
        return ans


if __name__ == "__main__":
    a = Solution().lengthOfLongestSubstring("abcabcbb")
    print(a)
    a = Solution().lengthOfLongestSubstring("bbbbb")
    print(a)
    a = Solution().lengthOfLongestSubstring("pwwkew")
    print(a)
