from collections import defaultdict


class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        n = len(answerKey)
        left = ans = 0
        freqMap = defaultdict(int)
        for right in range(n):
            v = answerKey[right]
            freqMap[v] += 1
            while freqMap["T"] > k and freqMap["F"] > k:
                freqMap[answerKey[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans


if __name__ == "__main__":
    a = Solution().maxConsecutiveAnswers("TTFTTFTT", 1)
    print(a)
