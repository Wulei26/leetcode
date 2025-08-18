from typing import List


class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        p = q = 0
        ans = []
        for x, y in zip(A, B):
            p = p | 1 << x
            q = q | 1 << y
            ans.append((p & q).bit_count())
        return ans


if __name__ == "__main__":
    A = [1, 3, 2, 4]
    B = [3, 1, 2, 4]
    a = Solution().findThePrefixCommonArray(A, B)
    print(a)
