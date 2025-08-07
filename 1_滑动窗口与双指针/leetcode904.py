from typing import List
from collections import defaultdict


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        ans = 0
        left = 0
        freqmap = defaultdict(int)  ##记录窗口中水果种类
        for right in range(n):
            v = fruits[right]
            freqmap[v] += 1
            while len(freqmap) > 2:
                freqmap[fruits[left]] -= 1
                if freqmap[fruits[left]] == 0:
                    del freqmap[fruits[left]]
                left += 1

            ans = max(ans, right - left + 1)
        return ans


if __name__ == "__main__":
    A = Solution().totalFruit([1, 2, 3, 2, 2])
    print(A)
    A = Solution().totalFruit([3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4])
    print(A)
